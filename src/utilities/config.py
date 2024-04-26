from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

PROJECT_SETUP = {
    "project_id": "ocrdocumentai-419906",
    "location": "us",
    "processor_id": "ffec49331ad6da12",
    "endpoint": "us-documentai.googleapis.com",     
}
