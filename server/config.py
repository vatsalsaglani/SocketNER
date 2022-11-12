import os
from dotenv import load_dotenv

load_dotenv()

class MODEL_PATH:
    path = os.environ.get("MODEL_PATH")