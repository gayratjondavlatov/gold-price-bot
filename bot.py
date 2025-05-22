import os
from telegram.ext import Updater, CommandHandler, CallbackContext, JobQueue
from telegram import Update
from datetime import datetime
import pytz
import requests

TOKEN = os.environ["8029323062:AAEp2apx2GP6SFq7CbxQCEcsRNwafvPf1c0"]
CHAT_ID = int(os.environ["499841895"])

def get_gold_price():
    # Bu yerga real API yoki parser kodini qo‘shing
    return "Bugungi oltin narxi: 1g = 745,000 so'm (test ma'lumot)"

def start(update: Update, context: CallbackContext):
    price = get_gold_price()
    update.message.reply_text(price)

def daily_callback(context: CallbackContext):
    price = get_gold_price()
    context.bot.send_message(chat_id=CHAT_ID, text=price)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    # JobQueue yaratish
    job_queue = updater.job_queue

    # Asia/Tashkent vaqt zonasini o‘rnatamiz
    tz = pytz.timezone('Asia/Tashkent')

    # Har kuni soat 9:00 da ishga tushadigan job qo‘shamiz
    job_queue.run_daily(daily_callback, time=datetime.time(9, 0, 0, tzinfo=tz))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
