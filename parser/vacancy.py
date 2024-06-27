import requests
import json

def get_data(text):
    i=0
    for page in range(20):
        data = requests.get(f"https://api.hh.ru/vacancies?page={page}&per_page=100&text={text}").json()
        for item in data["items"]:
            yield item

def get_vacancy(item):
    # if salary:= item["salary"]["from"]: pass
    # elif salary: 

    vacancy = {
        "id": item["id"],
        "name": item["name"],
        "city": item["area"]["name"],
        "schedule": item["id"],
        "experience": item["experience"]["name"],
        "employment": item["employment"]["name"],
        "requirement": item["snippet"]["requirement"],
        "responsibility": item["snippet"]["responsibility"],
        "salary": item["salary"],
        # "currency": item["salary"]["currency"]
    }
    return vacancy

if __name__ == "__main__":
    vac = []
    counter = 0
    for link in get_data("python"):
        vacancy = get_vacancy(link)
        vac.append(vacancy)
        print(vacancy)
    with open("vacancy.json", "w") as f:
        json.dump(vac, f, indent=4)
