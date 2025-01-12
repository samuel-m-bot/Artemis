from .client import NotionClient

__all__ = ['NotionClient']

PACKAGE_VERSION = '0.0.1'

def initialize_package():
    print(f'Initialising Notion Integration Package v{PACKAGE_VERSION}')

initialize_package()
