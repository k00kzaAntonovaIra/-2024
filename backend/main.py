from fastapi import FastAPI
from db import insert, select_by_params, create_table
from parser_vacancy import search
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()


app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
origins = [
    "http://localhost:5173"
    "http://127.0.0.1:5173"
]

class Vacancy(BaseModel):
    id: int
    name: str
    city: str
    experience: str
    employment: str
    requirement: str
    responsibility: str 
    salary: str
    link: str



@app.get("/")
def default():
    try:
        create_table()
        return "Status code 200"
    except Exception as e:
        return f"{e}"

@app.get("/vacancy")
def get_create_vacancy(text: str = None, experience:str = None) -> list[dict]:
    try:
        data = search(text, experience)
        insert(data)
        return data
    except Exception as e:
        return f"{e}"
    


@app.get("/vacancies/params")
def get_params(city: str | None = None, salary: str | None = None, employment: str | None = None):
    try:
        d=[]
        data = select_by_params(city, salary, employment)
        for i in data:
            d.append({"id":i[0], "name":i[1], "city":i[2], "experience":i[3], "employment":i[4], "requirement":i[5], "responsibility":i[6], "salary":i[7], "link":i[8]})
        return d
    except Exception as e:
        return f"{e}"
