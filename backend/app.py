from flask import Flask, jsonify, request
from flask_cors import CORS
from service import VacancyService
import logging

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)

vacancy_service = VacancyService()


@app.route('/add_search_parameters', methods=['POST'])
def add_search_parameters():
    data = request.json
    vacancy_service.update_vacancies(data['text'], data['experience'], data['schedule'], data['area'])
    return jsonify({'message': 'Параметры поиска добавлены и вакансии обновлены'}), 201


@app.route('/vacancies', methods=['GET'])
def get_vacancies():
    vacancies = vacancy_service.get_vacancies()
    return jsonify(vacancies)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
