import psycopg2
from env import DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT
import sys
sys.path.append('C:\\Users\\ira\\OneDrive\\Документы\\GitHub\\Uchebnaya_practica_june-july-2024\\parser') 
import vacancy
# from vacancy 
import time 

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port = DB_PORT
)


# cur = conn.cursor()

# def insert(data, conn):
#     cur = conn.cursor()
#     try:
#         insert_query = """INSERT INTO vacancy_table (id, name, city, schedule, experience, employment, requirement, responsibility, salary, link)
#                   VALUES (%(id)s, %(name)s, %(city)s, %(schedule)s, %(experience)s, %(employment)s, %(requirement)s, %(responsibility)s, %(salary)s, %(link)s)"""

#         cur.execute(insert_query, data)
        
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         conn.commit()
#         cur.close()  


cur = conn.cursor()
cur.execute("ALTER TABLE vacancy_table ALTER COLUMN salary SET DATA TYPE varchar;")
conn.commit()
cur.close()
# for link in vacancy.get_data("менеджер"):
#     vac = vacancy.get_vacancy(link)
#     insert(vac, conn)
#     time.sleep(0.05)
conn.close()

# cur.execute("CREATE TABLE vacancy_table (id int primary key, name varchar, city varchar, schedule varchar, experience varchar, employment varchar, requirement varchar, responsibility varchar, salary json, link varchar);")

# cur.execute("SELECT * FROM vacancy_table;")
# a=cur.fetchone()
# print(a)

# conn.commit()

# cur.close()

# cur.execute("CREATE TABLE vacancy_table (id int primary key, name varchar, city varchar, schedule varchar, experience varchar, employment varchar, requirement varchar, responsibility varchar, salary json, link varchar);")

# cur.execute("DELETE FROM vacancy_table WHERE id = 102756090")
# data = {'id': '102756090', 
#         'name': 'Методист по информатике', 
#         'city': 'Москва', 
#         'schedule': '102756090', 
#         'experience': 'От 3 до 6 лет', 
#         'employment': 'Полная занятость', 
#         'requirement': 'Знание одного из языков программирования на уровне применения ООП. (В приоритете <highlighttext>Python</highlighttext>, C++). Опыт разработки материалов для гос.экзаменов (ЕГЭ, ОГЭ...', 
#         'responsibility': 'Мониторинг существующего рынка учебно-методических материалов в целях поиска контента, соответствующего Персонализированной модели образования (далее – ПМО) и Платформе СберКласс (далее...', 
#         'salary': None, 
#         'link': 'https://hh.ru/vacancy/102756090?from=applicant_recommended&hhtmFrom=main'
#         }


# def create(conn):
#     cur = conn.cursor()
#     cur.execute("CREATE TABLE vacancy_table (id int PRIMARY KEY, name varchar, city varchar, schedule varchar, experience varchar, employment varchar, requirement varchar, responsibility varchar, salary jsonb);")
#     cur.fetchone()
#     conn.commit()
#     cur.close()
#     conn.close()


# def select(conn, filter_text, c_name):
#     cur = conn.cursor()
#     query = f"SELECT * FROM vacancy_table WHERE column_name = {c_name};"  # Замените column_name на имя столбца, по которому хотите фильтровать
#     cur.execute(query, (filter_text,))
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     cur.close()
