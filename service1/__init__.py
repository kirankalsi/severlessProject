import logging
import azure.functions as func
import requests
from azure.cosmos import CosmosClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numstring = requests.get('https://serverlessproject.azurewebsites.net/api/service2?code=SJYtXl8T8CgYuOpJcTi3v024/7CtCA6JQA/YM5wYLJsQPPa/zKN3gg==').text
    letterstring = requests.get('https://serverlessproject.azurewebsites.net/api/service3?code=wLj0EOvK4KivawcmHPuWshg3QifygU3flAJKEYaJnh723aHRf53pLw==').text

    username = ""
    for i in range(5):
        username += numstring[i] + letterstring[i]

    endpoint = 'https://username-db.documents.azure.com:443/'
    key = 'rTSqFSYaCRns0rqPbvSaXOVxXbs7PvZIwXOGpeu9abNsGoLcEhA26wUrpKIFwogfRaZismXgJyHM4MbOExpitg=='
    client = CosmosClient(endpoint, key)

    database_name = "username-db"
    database = client.create_database_if_not_exists(id=database_name)

    container_name = "Container1"
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/username")
    )
    username_to_add = {
        "id": username
    }
    container.create_item(body=username_to_add)

    return username
