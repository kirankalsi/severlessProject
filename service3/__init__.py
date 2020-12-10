import logging
import azure.functions as func
from string import ascii_lowercase
import random


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    letterstring = ''.join(random.choice(ascii_lowercase) for i in range(5))
    return letterstring