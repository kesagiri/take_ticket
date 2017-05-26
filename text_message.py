import telebot
import json
import requests
import constants


bot = telebot.TeleBot(constants.token)


def text_commands(message):
    if message.text == "сколько тикетов?":
        r = requests.get('https://estimator.timeweb.net/api.php?module=analytics&method=monitoringData&dep='
                         'clients&token=9ZFR9zhuFdhtJp0wCQ1H5y8DpExD3RqJdX0A81kbT71hmmOSpO221w89IKw0')
        ob = r.json()
        bot.send_message(message.chat.id, "Свободных тикетов: " + json.dumps(ob['cf']) + "\n" "Тикетов в работе: " +
                         json.dumps(ob['c']) + "\n\n" + "Ещё вопросы?")
    else:
        bot.send_message(message.chat.id, "...")

