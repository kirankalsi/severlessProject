import logging
import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numstring = requests.get().text
    letterstring = requests.get().text

    username = ''.join(numstring + letterstring) for i in range(5))