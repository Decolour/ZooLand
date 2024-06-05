import random
import schedule
import time
import asyncio
from telegram import Bot
from telegram.error import BadRequest

# Ваш токен, полученный от BotFather
TOKEN = '7139445889:AAGejXoPmbRoJlbmCuNRmobLQAftT-P9W-s'
CHAT_ID = '-4289291842'  # ID чата, куда будут отправляться цитаты



# Функция для чтения цитат из файла
def read_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = file.read().strip().split('\n\n\n')
    return [quote for quote in quotes if quote.strip()]


# Асинхронная функция для отправки случайной цитаты
async def send_quote(bot, quotes):
    quote = random.choice(quotes)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=quote.strip())
    except BadRequest as e:
        print(f"Failed to send message: {e}")


async def scheduled_job(quotes):
    bot = Bot(token=TOKEN)
    await send_quote(bot, quotes)


def run_scheduled_job(quotes):
    asyncio.run(scheduled_job(quotes))


def main():
    quotes = read_quotes('../First_rep/quotes.txt')  # Загрузка цитат из файла

    schedule.every().day.at("09:50").do(run_scheduled_job, quotes)  # Установите время по вашему желанию

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
