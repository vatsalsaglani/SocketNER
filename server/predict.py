import os
import re
import json
from typing import List, Dict, Union, Tuple
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


class NERPredictor:
    """NER Predictor Instance
    """
    def __init__(self, model_path: str):
        """Initializes the NER Predictor

        Args:
            model_path (str): Path To Model Files
        """
        self.model_path = model_path
        print(f"LOADING TOKENIZER")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        print(f"LOADED TOKENIZER")
        print(f"LOADING MODEL")
        self.model = AutoModelForTokenClassification.from_pretrained(
            self.model_path)
        print(f"LOADED MODEL")
        self.nlp_pipeline = pipeline("ner",
                                     model=self.model,
                                     tokenizer=self.tokenizer)

    def __combine_start_end__(self, text: str,
                              results: List[Dict]) -> List[Dict]:
        """Combines consecutive same entity types into one

        Args:
            text (str): Input Text
            results (List[Dict]): NER Result from the pipeline

        Returns:
            List[Dict]: Combined NER Result
        """
        index = 0
        current = None
        output = []
        while index < len(results):
            current = results[index].get("entity")
            start = results[index].get("start")
            end = results[index].get("end")
            index += 1
            while index < len(results) and results[index].get(
                    "entity") == current:
                end = results[index].get("end")
                index += 1
            output.append({
                "entity": current,
                "start": start,
                "end": end,
                "text": text[start:end]
            })
        return output

    def __clean_entity__(self, result: List[Dict]) -> List[Dict]:
        """Remove the B, I in entity

        Args:
            result (List[Dict]): NER Results

        Returns:
            List[Dict]: NER Results
        """
        [e.update({"entity": e.get("entity").split("-")[-1]}) for e in result]
        return result

    def __tag_input_text__(self, text: str,
                           formatted_result: List[Dict]) -> List[Dict]:
        """Tagging parts of the sentences

        Args:
            text (str): Input Text
            formatted_result (List[Dict]): NER Result

        Returns:
            List[Dict]: Tagged Parts of Sentences
        """
        start_end = list(
            map(lambda r: (r.get("start"), r.get("end")), formatted_result))
        start_end = sorted(start_end, key=lambda se: se[0])
        index = 0
        op = []
        while index < len(text):
            if not index in list(map(lambda se: se[0], start_end)):
                lst = []
                start = index
                while not index in list(map(lambda se: se[0],
                                            start_end)) and index < len(text):
                    lst.append({"entity": "other", "char": text[index]})
                    index += 1
                op.append({
                    "entity":
                    "other",
                    "text":
                    "".join(list(map(lambda char: char.get("char"), lst))),
                    "start":
                    start,
                    "end":
                    index
                })
            else:
                rng = list(filter(lambda se: se[0] == index, start_end))[0]
                en = rng[-1]
                res = list(
                    filter(
                        lambda re: re.get("start") == index and re.get("end")
                        == en, formatted_result))[0]
                op.append({
                    "entity": res.get("entity"),
                    "text": text[index:en],
                    "start": index,
                    "end": en
                })
                index = en
        return op

    def predict_result(self, text: str) -> List[Dict]:
        """Given the text predicts the NER Result

        Args:
            text (str): Input Text

        Returns:
            List[Dict]: NER Result with Start and End index and entity types
        """
        ner_results = self.nlp_pipeline(text)
        ner_results = self.__clean_entity__(ner_results)
        results = self.__tag_input_text__(text, ner_results)
        return self.__combine_start_end__(text, results)


if __name__ == "__main__":
    pred_obj = NERPredictor("./bert-base-NER")
    # while True:
    text = "my name is Vatsal Saglani and I stay in Bangalore"
    print(text)
    print(json.dumps(pred_obj.predict_result(text), indent=4))
    text = "I stay in Bangalore and my name is Vatsal Saglani"
    print(text)
    print(json.dumps(pred_obj.predict_result(text), indent=4))
