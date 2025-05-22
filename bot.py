import os
import telegram
import requests
from telegram.ext import Updater, CommandHandler
from datetime import datetime
import pytz
import threading
import time

# Telegram sozlamalari
TOKEN = os.environ["8029323062:AAEp2apx2GP6SFq7CbxQCEcsRNwafvPf1c0"]
CHAT_ID = os.environ["499841895"]
bot = telegram.Bot(token=TOKEN)

# Oltin narxini olish funksiyasi (hozircha test ma'lumot)
def get_gold_price():
    # Bu yerga real parser yoki API qo‘shishingiz mumkin
    return "Bugungi oltin narxi: 1g = 745,000 so'm (test ma'lumot)"

# /start komandasi uchun funksiyasi
def start(update, context):
    price = get_gold_price()
    context.bot.send_message(chat_id=update.effective_chat.id, text=price)

# Har kuni soat 9:00 da xabar yuboruvchi fon funksiyasi
def schedule_daily_message():
    uz_tz = pytz.timezone('Asia/Tashkent')
    while True:
        now = datetime.now(uz_tz)
        if now.hour == 9 and now.minute == 0:
            price = get_gold_price()
            bot.send_message(chat_id=CHAT_ID, text=price)
            time.sleep(60)  # qayta yuborilishdan saqlanish uchun
        time.sleep(20)

# Botni ishga tushirish
def main():
    # Jadval uchun fon oqimni boshlash
    threading.Thread(target=schedule_daily_message).start()

    # Telegram komandalari
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

main()
