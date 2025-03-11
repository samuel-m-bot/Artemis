import os
from dotenv import load_dotenv

load_dotenv()

NOTION_KEY = os.getenv('NOTION_KEY')
NOTION_PAGE_ID = os.getenv('NOTION_PAGE_ID')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

DEBUG_MODE = os.getenv('DEBUG_MODE', 'False') 
