from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from sender import send_message_to_telegram
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

class MessageRequest(BaseModel):
    name: str
    tel: str

templates = Jinja2Templates(directory='frontend')

@app.get("/", tags=["Основная страница"], summary="Главная страница")
async def get_rio(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get("/policy", tags=["Политика"], summary="Страница с инфо о политике")
async def get_policy(request: Request):
    return templates.TemplateResponse(name='privacy-policy.html', context={'request': request})

@app.post("/rio", tags=["Заказать звонок"], summary="отправка форма с данными для заказа звонка")
async def send_message(client: MessageRequest):
    try:
        idChat = 376817201
        await send_message_to_telegram(idChat, "Имя: {}, телефон: {}".format(client.name, client.tel))
        return {"message": "Сообщение отправлено в Telegram!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при отправке сообщения: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True,  host="0.0.0.0", port=80)