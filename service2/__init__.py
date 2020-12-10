import logging
import azure.functions as func
from string import digits
import random


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    numstring = ''.join(random.choice(digits) for i in range(5))
    return numstring