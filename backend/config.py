from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    USER_AGENT = os.getenv('USER_AGENT')
    FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    FLASK_PORT = os.getenv('FLASK_PORT', 5000)
