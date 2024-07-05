import psycopg2
from env import DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT
from parser_vacancy import search


def insert(data: list[dict]):
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port = DB_PORT
    )
    cur = conn.cursor()

    try:
        for i in data:
            insert_query = """INSERT INTO vacancy_table (id, name, city, experience, employment, requirement, responsibility, salary, link)
                    VALUES (%(id)s, %(name)s, %(city)s, %(experience)s, %(employment)s, %(requirement)s, %(responsibility)s, %(salary)s, %(link)s)"""
            cur.execute(insert_query, i)    
            conn.commit()     
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:

        cur.close()  
        conn.close()

data = search("менеджер")
insert(data)

# def select_by_params(area, salary, employment):
#     conn = psycopg2.connect(
#         dbname=DB_NAME,
#         user=DB_USER,
#         password=DB_PASS,
#         host=DB_HOST,
#         port = DB_PORT
#     )
#     cur = conn.cursor()
#     cur = conn.cursor()
#     str_select = "SELECT * FROM vacancy_table"
#     if area or salary or employment:


#     cur.execute(str_select, )
#     cur.close()  
#     conn.close()





# cur.close()

# for link in vacancy.get_data("менеджер"):
#     vac = vacancy.get_vacancy(link)
#     insert(vac, conn)


# cur.execute("CREATE TABLE vacancy_table (id int primary key, name varchar, city varchar, schedule varchar, experience varchar, employment varchar, requirement varchar, responsibility varchar, salary json, link varchar);")

# cur.execute("SELECT * FROM vacancy_table;")
# a=cur.fetchone()
# print(a)

# conn.commit()

# cur.close()
# cur.execute("DELETE FROM vacancy_table;")
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
