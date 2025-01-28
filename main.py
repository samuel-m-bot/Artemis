from config import NOTION_PAGE_ID, NOTION_KEY
import os
from notion_client import Client

def main():
    print('Artemis has access to Notion page:', NOTION_PAGE_ID)
    notion = Client(auth=NOTION_KEY)
    list_users_response = notion.users.list()
    print(list_users_response)

if __name__ == '__main__':
    main()
