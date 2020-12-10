import logging
import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numstring = requests.get('https://serverlessproject.azurewebsites.net/api/service2?code=SJYtXl8T8CgYuOpJcTi3v024/7CtCA6JQA/YM5wYLJsQPPa/zKN3gg==').text
    letterstring = requests.get('https://serverlessproject.azurewebsites.net/api/service3?code=wLj0EOvK4KivawcmHPuWshg3QifygU3flAJKEYaJnh723aHRf53pLw==').text

    username = ""
    for i in range(5):
        username += numstring[i] + letterstring[i]
    return username
