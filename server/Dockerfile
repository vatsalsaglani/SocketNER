FROM python:3.8.0-slim
RUN apt-get update
RUN apt-get install git gcc -y
RUN apt-get clean
# RUN git lfs install
RUN git clone https://huggingface.co/dslim/bert-base-NER 
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 5010
ENTRYPOINT [ "python", "server.py" ]