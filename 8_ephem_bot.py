"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

'''
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}
'''

def greet_user(update, context):
    text = 'Вызван /start \n введите /planet объект ДД/MM/ГГГГ,\
    или только объект, если хотите узнать про сегодня'
    print(text)
    update.message.reply_text(text)

# для нижеописанной функции если через date.today() то формат вывода YYYY-MM-DD, но как его отворматировать простым стопосбом\
# , без перетасовки вызваных атрибутов в f-string или без перегрупировке в regex

def constellation (planet, user_date=date.today()):
    try:
        planet_time = eval(f'ephem.{planet.capitalize()}("{user_date}")')
        #planet_time = onvertion = exec(f'ephem.{planet}("{date}")') #это почему то не работает
        return f'Планета {planet.capitalize()} на дату {user_date} проходит в созвездии {ephem.constellation(planet_time)[1]}'
    except (TypeError, AttributeError):
        return 'Вы выбрали не зодиакальный объект'
        

def user_request(update, context):
    user_text = update.message.text.split()
    print(user_text)
    if len(user_text) >= 3:
      user_date = user_text[2]
    elif len(user_text) == 2:
      user_date = date.today()
    update.message.reply_text(constellation(user_text[1], user_date))


def main():
    mybot = Updater(settings.TOKEN, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", user_request))
    dp.add_handler(MessageHandler(Filters.text, user_request))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
