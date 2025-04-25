import sqlite3


def create_connection():
    return sqlite3.connect('vacancies.db')


def create_table():
    with create_connection() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS vacancies (
            id integer PRIMARY KEY,
            title text,
            url text,
            requirements text,
            responsibilities text,
            company_name text
            )
        """)


def clear_vacancies():
    with create_connection() as db:
        db.execute("DELETE FROM vacancies")


def insert_vacancy(vacancy_data):
    with create_connection() as db:
        db.execute('''INSERT OR IGNORE INTO vacancies 
                     (id, title, url, requirements, responsibilities, company_name) 
                     VALUES (?, ?, ?, ?, ?, ?)''', vacancy_data)


def get_all_vacancies():
    with create_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM vacancies")
        return cursor.fetchall()
