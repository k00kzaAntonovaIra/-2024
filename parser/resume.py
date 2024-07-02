import requests
from bs4 import BeautifulSoup
import fake_useragent
import json

def g(string):

    string = string.replace("\xa0", " ")
    string = string.replace("&nbsp;", " ")
    string = string.replace("&thinsp;", "")
    string = string.replace("\u2009", "")
    return string

def get_links(text):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=f"https://hh.ru/search/resume?text={text}&area=113&isDefaultArea=true&ored_clusters=true&order_by=relevance&search_period=0&logic=normal&pos=full_text&exp_period=all_time&page=1",
        headers={"user-agent":ua.random}
    )
    if data.status_code != 200:
        return
    soup = BeautifulSoup(data.content, "lxml")
    try:
        page_count = int(soup.find("div", attrs={"class":"pager"}).find_all("span",recursive=False)[-1].find("a").find("span").text)
    except:
        return
    for page in range(page_count):
        try:
            data = requests.get(
                url=f"https://hh.ru/search/resume?text={text}&area=113&isDefaultArea=true&ored_clusters=true&order_by=relevance&search_period=0&logic=normal&pos=full_text&exp_period=all_time&page={page}",
                headers={"user-agent":ua.random}
            )
            if data.status_code != 200:
                continue
            soup = BeautifulSoup(data.content, "lxml")
            for a in soup.find_all("a", attrs={"class":"bloko-link"}):
                yield f"https://hh.ru{a.attrs['href'].split('?')[0]}"
        except Exception as e:
            print(f"{e}")


def get_value(soup, attribute, default=""):
    try:
        value = g(soup.find(attrs=attribute).text)
        return value
    except AttributeError:
        return default
    
def get_resume(link):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url = link,
        headers={"user-agent":ua.random}
    )
    if data.status_code != 200:
        return
    soup = BeautifulSoup(data.content, "lxml")

    name = get_value(soup, {"class":"resume-block__title-text"})
    salary = get_value(soup, {"class": "resume-block__salary"})
    age = get_value(soup, {"data-qa": "resume-personal-age"})
    male = get_value(soup, {"data-qa": "resume-personal-gender"})
    job_s = get_value(soup, {"class": "resume-job-search-status"})
    expir = g(get_value(soup, {"resume-block__title-text resume-block__title-text_sub"}).replace("Опыт работы ", ""))

    try:
        skills = [tag.text for tag in soup.find(attrs={"class":"bloko-tag-list"}).find_all(attrs={"class":"bloko-tag__section bloko-tag__section_text"})]
    except:
        skills = []  

    resume = {
        "ДОЛЖНОСТЬ": name,
        "ПОЛ": male,
        "ВОЗРАСТ": age,
        "ПОИСК": job_s,
        "ЗАРПЛАТА": salary,
        "НАВЫКИ": skills,
        "ОПЫТ": expir,
        "ССЫЛКА": link

    }

    return resume

if __name__ == "__main__":
    resum = []
    counter = 0
    for link in get_links("python"):
        resume = get_resume(link)
        if resume["ДОЛЖНОСТЬ"]:
            print(resume)
            resum.append(resume)
            counter += 1
            if counter >= 20:
                break

    with open("resume.json", "w") as f:
        json.dump(resum, f, indent=4)