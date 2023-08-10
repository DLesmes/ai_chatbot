"""Settings module"""
import os
from dotenv import load_dotenv
load_dotenv()


class Settings:
    MACHINE = os.getenv("MACHINE")
    if MACHINE == "GCP":
        ROOT_PATH = "/chatbot"
    else:
        ROOT_PATH = ""

    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS")
    ALLOW_CREDENTIALS = os.getenv("ALLOW_CREDENTIALS")
    ALLOW_METHODS = os.getenv("ALLOW_METHODS")
    ALLOW_HEADERS = os.getenv("ALLOW_HEADERS")