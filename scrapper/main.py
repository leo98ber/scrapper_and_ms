import requests
import json

import os
import sys

import errors
import vars


def query_to_service(data):
    base_url = vars.URLS.get('base_url')
    microservice_url = f'{base_url}/'

    if data:
        response = requests.post(url=microservice_url, data=json.dumps(data),
                                 headers={'Content-Type': 'application/json'})

        if response.status_code == 201:
            os.system(f'echo Scrapping data was saved successfully: {data}')
        else:
            raise errors.UnexpectedErrorFromService('Failed save data')

    else:
        raise errors.DataNotFound('The scrapping provided invalid data')

    return True

def scrapper():
    pass


if __name__ == '__main__':
    is_successful = None
    try:
        params = sys.argv
        # data = {'name': 'beroes'}
        data = scrapper()
        is_successful = query_to_service(data)

    except errors.InvalidParameters as ex1:
        os.system(f'echo {ex1}')

    except errors.DataNotFound as ex2:
        os.system(f'echo Error while executing query_to_service: {ex2}')

    except errors.InvalidResponseData as ex3:
        os.system(f'echo Error while executing query_to_service: {ex3}')

    except errors.UnexpectedErrorFromService as ex4:
        os.system(f'echo Error running the service: {ex4}')

    except requests.exceptions.ConnectionError:
        os.system('echo Error calling the service: Failed to establish a new connection')

    except Exception as ex:
        os.system(f'echo An unexpected error has occurred: {ex}')
