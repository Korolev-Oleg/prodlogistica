from celery_config import app
from requests import get
from datetime import datetime
from .models import Vacancies
from config.settings.base import MEDIA_URL


def sort(vacancies: dict) -> None:
    """ Sorting vacancies by published with bubble algorithm
        :param vacancies: HeadHunter json response
    """
    datetime_pattern = "%Y-%m-%dT%H:%M:%S+%f"
    _sorted = False
    while not _sorted:
        _sorted = True
        for i in range(len(vacancies) - 1):
            cur_date_text = vacancies[i]['published_at']
            next_date_text = vacancies[i + 1]['published_at']
            cur_date = datetime.strptime(cur_date_text, datetime_pattern)
            next_date = datetime.strptime(next_date_text, datetime_pattern)
            if cur_date < next_date:
                vacancies[i], vacancies[i + 1] = vacancies[i + 1], vacancies[i]
                _sorted = False


@app.task
def update_vacancies() -> None:
    """ task updating vacancies from HeadHunter """
    response = get('https://api.hh.ru/vacancies?employer_id=649480')
    vacancies = response.json()['items']
    sort(vacancies)

    for vacancy in vacancies:
        new_vacancy = Vacancies()
        new_vacancy.title = vacancy['name']
        new_vacancy.description = vacancy['snippet']['responsibility']
        new_vacancy.published = datetime.strptime(vacancy['published_at'], "%Y-%m-%dT%H:%M:%S+%f")
        new_vacancy.url = vacancy['alternate_url']
        new_vacancy.normalize()
        if not new_vacancy.is_contained():
            new_vacancy.save()
