import sqlite3


class DatabaseManager:
    def __init__(self, db_name='vacancies.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS vacancies (
                    id integer PRIMARY KEY,
                    title text,
                    url text,
                    requirements text,
                    responsibilities text,
                    company_name text
                )
            """)
            conn.commit()

    def clear_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM vacancies")
            conn.commit()

    def insert_vacancy(self, vacancy):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO vacancies 
                (id, title, url, requirements, responsibilities, company_name) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                vacancy['id'],
                vacancy['name'],
                vacancy['alternate_url'],
                vacancy['snippet']['requirement'],
                vacancy['snippet']['responsibility'],
                vacancy['employer']['name']
            ))
            conn.commit()

    def get_all_vacancies(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vacancies")
            return cursor.fetchall()
