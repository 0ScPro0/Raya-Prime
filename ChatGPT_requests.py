import requests
import json
from icecream import ic

class ChatGPT:
    def __init__(self, PERSONAL_ACCESS_TOKEN : str, BOT_ID : str, USER_ID : str, API_URL : str) -> None:
        self.PERSONAL_ACCESS_TOKEN = PERSONAL_ACCESS_TOKEN
        self.BOT_ID = BOT_ID
        self.USER_ID = USER_ID
        self.API_URL = API_URL

    def send_request_to_ChatGPT(self, query):

        query = f"Тебе нужно ответить на вопрос кратко и четко, без лишних слов, приветсвий и тд. Просто вопрос - ответ. Вопрос: {query}"

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