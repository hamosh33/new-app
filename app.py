import telebot

TOKEN = '6036880264:AAEe_hX4N-wXmuHUT37X2k-zqkbBXQwsbPo'  # استبدل هذا بتوكن بوتك الخاص
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا، أنا بوت تليجرام الخاص بك!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
