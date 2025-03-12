import requests
import logging


class HeadHunterAPI:
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "Your User Agent"}

    def fetch_vacancies(self, search_text, experience, schedule, area, page=1, per_page=100):
        params = {
            "text": search_text,
            "page": page,
            "per_page": per_page
        }
        if experience != 'any':
            params['experience'] = experience
        if schedule != 'any':
            params['schedule'] = schedule
        if area != 'any':
            params['area'] = area

        response = requests.get(self.base_url, params=params, headers=self.headers)
        if response.status_code == 200:
            return response.json()['items']
        else:
            logging.error(f"Ошибка при запросе к API: {response.status_code}")
            return []
