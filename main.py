from config import NOTION_PAGE_ID, NOTION_KEY, NOTION_DATABASE_ID
import json
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

    response = notion.databases.query(database_id=NOTION_DATABASE_ID)

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    tasks = []
    for item in response["results"]:
        task = {
            "id": item["id"],
            "name": (
                item["properties"]["Name"]["title"][0]["text"]["content"]
                if "Name" in item["properties"] and item["properties"]["Name"]["title"]
                else "Untitled"
            ),
            "created_time": item["created_time"],
            "last_edited_time": item["last_edited_time"]
        }

        #There is a checkbox for each day (default to False if missing)
        for day in days_of_week:
            task[day] = (
                item["properties"][day]["checkbox"]
                if day in item["properties"] and "checkbox" in item["properties"][day]
                else False
            )

        tasks.append(task)

    json_output = json.dumps(tasks, indent=4)

    print(json_output)

if __name__ == '__main__':
    main()
