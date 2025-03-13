import httpx

# Функция для отправки сообщения в Telegram
async def send_message_to_telegram(chat_id: str, text: str):
    token = "7594090227:AAG4Dceveh2OBP9mripXQkDl5WOzCScqNW0"  # Токе бота
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json={"chat_id": chat_id, "text": text})
        response.raise_for_status()  # Поднимает исключение для статусов 4xx и 5xx