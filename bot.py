import requests
import time
import os
from datetime import datetime
import pytz
import telegram

# Telegram sozlamalari
TOKEN = os.environ["8029323062:AAEp2apx2GP6SFq7CbxQCEcsRNwafvPf1c0"]
CHAT_ID = os.environ["499841895"]
bot = telegram.Bot(token=TOKEN)

# Oltin narxini olish funksiyasi (mahalliy sayt URL’ini o‘zingiz yangilaysiz)
def get_gold_price():
    # Hozircha oddiy test ma’lumoti
    return "Bugungi oltin narxi: 1g = 745,000 so'm (misol uchun)"

# Har kuni soat 09:00 da yuborish
def run_daily():
    uz_tz = pytz.timezone('Asia/Tashkent')
    while True:
        now = datetime.now(uz_tz)
        if now.hour == 9 and now.minute == 0:
            gold_price = get_gold_price()
            bot.send_message(chat_id=CHAT_ID, text=gold_price)
            time.sleep(60)  # 1 daqiqa kutadi, bir necha marta jo‘natmaslik uchun
        time.sleep(20)

run_daily()
