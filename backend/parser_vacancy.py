import httpx


def fetch_url(url):
    with httpx.Client() as client:
        response = client.get(url)
        return response.json()


def fetch_all(urls):
    tasks = [fetch_url(url) for url in urls]
    results = [task for task in tasks]
    return results


def search_for_text(text) -> list[str]:
    urls = [
        f"https://api.hh.ru/vacancies?page={page}&per_page=100&text={text}"
        for page in range(20)
    ]
    return urls


def get_vacancy(item):
    id = item["id"]
    if item["salary"] and item["salary"]["from"]:
        salary = item["salary"]["from"]
    elif (item["salary"] is not None) and (item["salary"]["to"] is not None):
        salary = item["salary"]["to"]
    else:
        salary = ""
    vacancy = {
        "id": id,
        "name": item["name"],
        "city": item["area"]["name"],
        "experience": item["experience"]["name"],
        "employment": item["employment"]["name"],
        "requirement": item["snippet"]["requirement"],
        "responsibility": item["snippet"]["responsibility"],
        "salary": salary,
        "link": f"https://hh.ru/vacancy/{id}?from=applicant_recommended&hhtmFrom=main"
    }
    return vacancy


def search(query: str) -> list[dict]:
    results = fetch_all(search_for_text(query))
    try:
        vacancies = []
        for result in results:
            for item in result["items"]:
                vacancy = get_vacancy(item)
                vacancies.append(vacancy)
    except Exception:
        pass
    return vacancies


if __name__ == "__main__":
    search_results = search('химик')
    print(search_results)
