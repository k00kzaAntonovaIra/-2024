from fastapi import FastAPI
from backend.db import insert, select_by_params
from backend.parser_vacancy import search
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()


app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
# # origins = [
# #     "http://localhost:5173"
# #     "http://127.0.0.1:5173"
# # ]

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
def default() -> Response:
    return Response(status_code=418, content='Nothing to do at the root.')

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
        data = select_by_params(city, salary, employment)
        return data
    except Exception as e:
        return f"{e}"
