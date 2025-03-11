from .settings import NOTION_KEY, NOTION_PAGE_ID, NOTION_DATABASE_ID, DEBUG_MODE


__all__ = ['NOTION_KEY', 'NOTION_PAGE_ID', 'NOTION_DATABASE_ID', 'DEBUG_MODE']

PACKAGE_VERSION = '0.0.1'

def print_config():
    print(f'Initialising Config Package v{PACKAGE_VERSION}')
    print("Configuration Loaded:")
    print(f"SECRET_KEY: {'*' * len(NOTION_KEY) if NOTION_KEY else 'Not Set'}")
    print(f"NOTION_PAGE_ID: {NOTION_PAGE_ID}")
    print(f"DEBUG_MODE: {DEBUG_MODE}")

print_config()
