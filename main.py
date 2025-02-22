from config import NOTION_PAGE_ID, NOTION_KEY
import os
from notion_client import Client

notion = Client(auth=NOTION_KEY)

def find_database(page_id):
    response = notion.blocks.children.list(block_id=page_id)
    
    for block in response["results"]:
        if block["type"] == "child_database":
            return block["id"]  
    
    return None 

def main():
    print('Artemis has access to Notion page:', NOTION_PAGE_ID)
    list_users_response = notion.users.list()
    print(list_users_response)
    print(notion.pages.retrieve(NOTION_PAGE_ID))

    database_id = find_database(NOTION_PAGE_ID)

    if database_id:
        print(f"Found Database ID: {database_id}")
        tasks = notion.databases.query(database_id)
        print(tasks)  
    else:
        print("No database found in this page.")

if __name__ == '__main__':
    main()
