from database import DatabaseManager
from api import HeadHunterAPI
import logging


class VacancyService:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.hh_api = HeadHunterAPI()

    def update_vacancies(self, search_text, experience, schedule, area):
        self.db_manager.clear_table()
        for page in range(1, 21):
            vacancies = self.hh_api.fetch_vacancies(search_text, experience, schedule, area, page)
            for vacancy in vacancies:
                self.db_manager.insert_vacancy(vacancy)
        logging.info("Вакансии успешно обновлены.")

    def get_vacancies(self):
        vacancies = self.db_manager.get_all_vacancies()
        return [{
            'id': vacancy[0],
            'title': vacancy[1],
            'url': vacancy[2],
            'requirements': vacancy[3],
            'responsibilities': vacancy[4],
            'company_name': vacancy[5]
        } for vacancy in vacancies]
