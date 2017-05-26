import telebot
import text_message
import keyboards
import constants


bot = telebot.TeleBot(constants.token)


@bot.message_handler(commands=['start'])
def handle_text(message):
    keyboards.start(message)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    keyboards.stop(message)


@bot.message_handler(commands=['help'])
def handle_help(message):
    keyboards.help(message)


@bot.message_handler(commands=['ticket'])
def handle_help(message):
    keyboards.ticket(message)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text_message.text_commands(message)


bot.polling(none_stop=True)
bot.polling(none_stop=True, interval=0)