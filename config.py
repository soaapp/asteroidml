# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # loads from .env file

NASA_API_KEY = os.getenv("NASA_API_KEY")
