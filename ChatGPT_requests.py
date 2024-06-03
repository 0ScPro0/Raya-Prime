import requests
import json
from icecream import ic

class ChatGPT:
    def __init__(self) -> None:
        self.PERSONAL_ACCESS_TOKEN = "pat_14y3pTGIb9hBdFpEeFn7ezgtH8jM8eWcuANdWDCsYXOG85MGdLF0cEgFHge21RO0"
        self.BOT_ID = "7355571501997293573"
        self.USER_ID = "7355571474067062789"
        self.API_URL = "https://api.coze.com/open_api/v2/chat"

    def send_request_to_ChatGPT(self, query):
        headers = {
            "Authorization": f"Bearer {self.PERSONAL_ACCESS_TOKEN}",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept": "*/*"
        }

        data = {
            "bot_id": self.BOT_ID,
            "user": self.USER_ID,
            "query": query,
            "stream": False
        }

        response = requests.post(self.API_URL, headers = headers, data = json.dumps(data))

        if response.status_code == 200:
            response_data = response.json()

            if response_data["code"] == 0:  # проверка успешности запроса
                messages = response_data.get("messages", [])

                for message in messages:
                    if message["role"] == "assistant" and message["type"] == "answer":
                        return message["content"]
            else:
                ic("Ошибка в запросе:", response_data["msg"])

        else:
            ic("Ошибка HTTP:", response.status_code)