from fastapi import FastAPI, HTTPException, APIRouter
from db import insert
from parser_vacancy import search

# from db import insert
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# from parser_vacancy import search 


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
def get_create_vacancy(text: str = None) -> list[dict]:
    try:
        data = search(text)
        insert(data)
        return data
    except Exception as e:
        return f"{e}"
    

# @router.get("/vacancies/params")
# async def get_params(area: str | None = None, salary: str | None = None, employment: str | None = None):
#     try:
        