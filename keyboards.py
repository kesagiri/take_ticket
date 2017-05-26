import telebot
import time
from selenium import webdriver
import constants


bot = telebot.TeleBot(constants.token)


def start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/help', '/ticket')
    user_markup.row('сколько тикетов?')
    bot.send_message(message.from_user.id, "Клавиатура включена. Для получения справки нажмите /help", reply_markup=user_markup)


def stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Клавиатура отключена, для включения ввести /start", reply_markup=hide_markup)


def help(message):
    bot.send_message(message.chat.id, "Могу показать сколько тикетов свободных и в работе, а также взять свободный"
                                      " тикет в работу")


def ticket(message):
    driver = webdriver.Chrome("C:/Users/a.dubchak/IdeaProjects/chromedriver.exe")
    driver.get('https://staff2.timeweb.ru/tickets/picker/pick?service=clients')
    element = driver.find_element_by_id("loginform-username")
    element.send_keys("")  # логин
    element1 = driver.find_element_by_id("loginform-password")
    element1.send_keys("")  # пароль
    element2 = driver.find_element_by_name("login-button")
    element2.click()
    time.sleep(1)
    if driver.title == "Ошибка":
        bot.send_message(message.chat.id, "Свободных тикетов нет")
        print("Свободных тикетов нет")
        driver.close()
    else:
        bot.send_message(message.chat.id, "Тикет в работе" + "\n" + driver.title)
        print("Тикет в работе")
        print(driver.title)

