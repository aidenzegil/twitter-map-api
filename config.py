from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
auth_token = os.getenv('AUTH_TOKEN')
pat = os.getenv('PERSONAL_ACCESS_TOKEN')
pat_secret = os.getenv('PAT_SECRET')