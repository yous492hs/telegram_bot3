import os
import telebot

# نقرأ التوكن من متغيّر البيئة
TOKEN = os.environ.get("TOKEN")

# نتاكد التوكن موجود
if not TOKEN:
    print("Error: TOKEN is not set in environment variables.")
    exit()

# إنشاء البوت
bot = telebot.TeleBot(TOKEN)

# رد بسيط على أي رسالة
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "هلا حبي، استلمت رسالتك!")

# تشغيل البوت
print("البوت اشتغل...")
bot.infinity_polling()
