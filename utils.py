import json
import typing

import requests
from bs4 import BeautifulSoup


def _parse_settings() -> str:
    with open("settings.json") as settings:
        settings = json.load(settings)
        session = settings.get("session")
        # идем в cookies и ищем там session
        assert session, "forgot to specify session"
        return session


def get_input_data(day: int) -> str:
    headers = {"Cookie": f"session={_parse_settings()}"}
    response = requests.get(f"https://adventofcode.com/2025/day/{day}/input", headers=headers)
    data = response.text
    return data


def post_answer(day: int, part: typing.Any, answer: typing.Any) -> None:
    headers = {"Cookie": f"session={_parse_settings()}"}
    data = {"level": str(part), "answer": str(answer)}
    response = requests.post(f"https://adventofcode.com/2025/day/{day}/answer", data=data, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("main").find("article").get_text()
    print(result)
