# app/core/config.py
import os

from dotenv import load_dotenv

API_V1_STR = "/api"

load_dotenv(".env")

PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI ML Example")