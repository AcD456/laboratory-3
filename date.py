import re
from datetime import datetime
import requests

#регулярное выражение
date_regex = r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}\b'

def is_valid_date(date_str):
    try:
        # Попытка создать объект datetime из строки
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def find_dates_in_text(text):
    potential_dates = [match.group(0) for match in re.finditer(date_regex, text)]
    # Фильтрация только корректных дат
    valid_dates = [date for date in potential_dates if is_valid_date(date)]
    return valid_dates


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def fetch_url_content(url):
    response = requests.get(url)
    response.raise_for_status()  # Проверка на успешный запрос
    return response.text