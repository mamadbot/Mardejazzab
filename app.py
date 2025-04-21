import os
import threading
from flask import Flask
import telebot
from telebot import types
import random

# تنظیمات اولیه
app = Flask(__name__)
TOKEN = os.getenv('TOKEN', '7574617425:AAHAIHVm7UGbFkOlK4yhDxoU5uRQC_QEd8E_BOTFATHER')  # از متغیر محیطی یا مستقیم
bot = telebot.TeleBot(TOKEN)
PORT = int(os.getenv('PORT', 10000))

# لیست پاسخ‌های شیت تست
sheet_test_responses = [
    "تو زیادی مطمئن به‌نظر میای → خب آره، چون می‌دونم چی می‌خوام.",
    "تو حتماً با همه دخترا اینطوری حرف می‌زنی → نه، فقط با اونایی که جذبم می‌کنن.",
    "تو خیلی مغروری → می‌گن غرورم جذابه!",
    "تو فقط دنبال سرگرمی هستی → اگه سرگرم‌کننده باشی، چرا که نه!",
    "فکر نکن خیلی خاصی → نمی‌فکر کنم، مطمئنم!",
    "تو زیادی راحتی → راحتی با اعتماد به نفسه نه بی‌ادبی.",
    "تو خودتو گرفتی → نه، فقط استاندارد دارم.",
    "همه پسرا مثل همن → خوشحالم که متوجه شدی من فرق دارم.",
    "تو خیلی خودتو تحویل می‌گیری → از خودم مراقبت می‌کنم، این بده؟",
    "چرا اینقدر به خودت مطمئنی؟ → چون تمرینش کردم و خودمو می‌شناسم."
]

# راه‌اندازی وب‌سرور
@app.route('/')
def home():
    return "ربات مرد جذاب فعال است! برای مدیریت از /start در تلگرام استفاده کنید."

# هندلرهای ربات
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("آموزش شیت تست‌ها"),
        types.KeyboardButton("شوخی دو پهلو"),
        types.KeyboardButton("داستان‌سرایی جذاب"),
        types.KeyboardButton("دختر مناسب رابطه"),
        types.KeyboardButton("تبدیل به مرد آلفا")
    )
    bot.send_message(
        message.chat.id,
        "به ربات مرد جذاب خوش اومدی!\nاز منوی زیر انتخاب کن:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "آموزش شیت تست‌ها":
        bot.send_message(message.chat.id, random.choice(sheet_test_responses))
    elif message.text == "شوخی دو پهلو":
        bot.send_message(message.chat.id, "بزودی شوخی‌های خاص اضافه میشه!")
    elif message.text == "داستان‌سرایی جذاب":
        bot.send_message(message.chat.id, "در حال آماده‌سازی داستان‌های باحال...")
    elif message.text == "دختر مناسب رابطه":
        bot.send_message(message.chat.id, "نشونه‌های دختر سالم: مرز، رشد، صداقت.")
    elif message.text == "تبدیل به مرد آلفا":
        bot.send_message(message.chat.id, "مرد آلفا بودن یعنی هدایت کردن نه کنترل.")

# اجرای همزمان ربات و وب‌سرور
def run_bot():
    bot.infinity_polling()

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=PORT)
