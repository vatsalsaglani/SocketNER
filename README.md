# Blazing Fast NER experience with WebSockets using FastAPI

![Socket NER](SocketNER_8x.mp4)

This repo contains a minimal UI built using **[SvelteKit](https://kit.svelte.dev/)**. The backend is a **[FastAPI](https://fastapi.tiangolo.com/)** WebSocket server. The backend exposes a pre-trained _Named Entity Recognizer (NER)_ model. The pre-trained model is trained by _[David S. Lim](https://huggingface.co/dslim)_ and it available under _[bert-base-NER](https://huggingface.co/dslim/bert-base-NER)_ on **[HuggingFace](https://huggingface.co/)**. The NER model was very much important for building this demo very quickly and hence the recognition.

## How to run this?

_Note:_ Please have **[Docker](https://www.docker.com/)** installed in your machine

1. Clone the repository
```
git clone https://github.com/vatsalsaglani/SocketNER.git
```
2. Move inside the **SocketNER** folder and run
```
docker-compose up
```
3. Once executed the above command the UI will be available on port _3000_