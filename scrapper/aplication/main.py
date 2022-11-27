import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from time import sleep
import json

import os

import errors
import vars


def query_to_service(scrapping_data):
    base_url = vars.URLS.get('base_url')
    microservice_url = f'{base_url}/'

    if scrapping_data:
        response = requests.post(url=microservice_url, data=json.dumps(scrapping_data),
                                 headers={'Content-Type': 'application/json'})

        if response.status_code == 201:
            os.system(f'echo Scrapping data was saved successfully: {scrapping_data}')
        else:
            raise errors.UnexpectedErrorFromService('Failed save data')

    else:
        raise errors.DataNotFound('The scrapping provided invalid data')

    return True


def find_ci(driver, document):
    driver.find_element(By.XPATH, f'//option[@value="{document.upper()}"]').click()
    id = driver.find_element(By.XPATH, '//input[@name="cedula"]')
    id.clear()
    cedula = int(input("\n\nIntroduzca su cedula: \n\n"))
    id.send_keys(cedula)
    sleep(random.uniform(1.0, 2.0))

    button = driver.find_element(By.XPATH, '//input[@title="Buscar"]')
    button.click()
    print("Buscando")

    sleep(random.uniform(2.0, 3.0))

    register = driver.find_elements(By.XPATH, '//td[@align="left"]')

    person_dates = []
    dates = []

    # assert len(
    #     register) == 22, "No se encontraron resultados, esto puede deberse a que introdujo una cedula invalida o inexistente"

    for date in register:
        date_person = date.text
        person_dates.append(date_person)

    for i in range(1, 11, 2):
        dates.append(person_dates[i])

    print("\n\nDATOS\n\n", dates)
    id.clear()

    return {'name': cedula}


def scrapper():
    driver = webdriver.Chrome()
    driver.get('http://www.cne.gob.ve/web/index.php')
    print("\n\nPagina lista\n\n")
    sleep(random.uniform(1.0, 2.0))

    input_ci = input("\n\nIndique que tipo de cedula posee?(V/E): ").lower()

    return find_ci(driver, input_ci)


if __name__ == '__main__':
    is_successful = None
    try:
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
