from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    AWS_ENDPOINT = os.getenv("AWS_ENDPOINT")
    AWS_REGION = os.getenv("AWS_REGION")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    QUEUE_NAME = os.getenv("QUEUE_NAME")


settings = Settings()