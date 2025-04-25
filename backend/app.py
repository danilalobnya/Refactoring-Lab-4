from flask import Flask, jsonify, request
from flask_cors import CORS
from database.db import create_table, get_all_vacancies
from services.vacancies import parse_vacancies
from config import Config

app = Flask(__name__)
CORS(app)

create_table()


@app.route('/add_search_parameters', methods=['POST'])
def add_search_parameters():
    data = request.json
    parse_vacancies(
        data['text'],
        data['experience'],
        data['schedule'],
        data['area']
    )
    return jsonify({'message': 'Параметры поиска добавлены и вакансии обновлены'}), 201


@app.route('/vacancies', methods=['GET'])
def get_vacancies_from_db():
    vacancies = get_all_vacancies()
    result = [{
        'id': vacancy[0],
        'title': vacancy[1],
        'url': vacancy[2],
        'requirements': vacancy[3],
        'responsibilities': vacancy[4],
        'company_name': vacancy[5]
    } for vacancy in vacancies]
    return jsonify(result)


if __name__ == '__main__':
    app.run(host=Config.FLASK_HOST, port=Config.FLASK_PORT)
