from dotenv import load_dotenv
import os
load_dotenv()

HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" else "https://release-gs.qa-playground.com/api/v1"
API_TOKEN = os.getenv('API_TOKEN')