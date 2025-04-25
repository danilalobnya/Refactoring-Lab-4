import requests
from ..database.db import clear_vacancies, insert_vacancy
from ..config import Config


def parse_vacancies(text, experience, schedule, area):
    url = "https://api.hh.ru/vacancies"
    headers = {"User-Agent": Config.USER_AGENT}

    clear_vacancies()

    for page in range(1, 21):
        params = {
            "text": text,
            "page": page,
            "per_page": 100
        }
        if experience != 'any':
            params['experience'] = experience
        if schedule != 'any':
            params['schedule'] = schedule
        if area != 'any':
            params['area'] = area

        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            vacancies = response.json()['items']
            for vacancy in vacancies:
                vacancy_data = (
                    vacancy['id'],
                    vacancy['name'],
                    vacancy['alternate_url'],
                    vacancy['snippet']['requirement'],
                    vacancy['snippet']['responsibility'],
                    vacancy['employer']['name']
                )
                insert_vacancy(vacancy_data)
        else:
            print(f"Request failed with status code: {response.status_code}")
