import csv
import json
import typing
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def get_input_data(day: int) -> str:
    headers = {"Cookie": f"session={_parse_settings()}"}
    response = requests.get(f"https://adventofcode.com/2025/day/{day}/input", headers=headers)
    data = response.text
    return data


def post_answer(day: int, part: int, answer: typing.Any) -> None:
    day = str(day)
    part = str(part)
    answer = str(answer)
    print(f"day: {day}, part: {part}, answer: {answer}")
    
    headers = {"Cookie": f"session={_parse_settings()}"}
    data = {"level": part, "answer": answer}
    response = requests.post(f"https://adventofcode.com/2025/day/{day}/answer", data=data, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    response = soup.find("main").find("article").get_text().replace("\n", "").replace("\r", "").strip()
    print(response)
    
    _log_output(day, part, answer, response)


def _parse_settings() -> str:
    with open("settings.json") as settings:
        settings = json.load(settings)
        session = settings.get("session")
        # идем в cookies и ищем там session
        assert session, "forgot to specify session"
        return session


def _log_output(day: str, part: str, answer: str, response: str) -> None:
    csv_file = Path(f"output/day{day}/part{part}.csv")
    is_file_exist = csv_file.exists()
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    csv_data = {
        "timestamp": datetime.now().isoformat(),
        "answer": answer,
        "response": response,
    }
    with open(csv_file, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(csv_data))
        if not is_file_exist:
            writer.writeheader()
        writer.writerow(csv_data)
