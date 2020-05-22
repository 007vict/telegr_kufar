from time import sleep
import telebot
import configparser
import lxml

import requests
from bs4 import BeautifulSoup

config = configparser.ConfigParser()
config.read('settings.ini')

FEED = config.get('Feed', 'feed')
BOT_TOKEN = config.get('Telegram', 'bot_token')
CHANNEL = config.get('Telegram', 'channel')

bot = telebot.TeleBot(BOT_TOKEN)

with requests.Session() as se:
    se.headers = {
        'authority': 'www.kufar.by',
        'method': 'GET',
        'path': '/ listings?size = 42 & sort = lst.d & cur = BYR & cat = 17010 & rgn = 1',
        'scheme': 'https',
        'accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange; v = b3; q = 0.9',
        'accept - encoding': 'gzip, deflate, br',
        'accept - language': 'ru - RU, ru; q = 0.9, en - US; q = 0.8, en; q = 0.7',
        'cache - control': 'max - age = 0',
        'cookie': '_gcl_au=1.1.1847513745.1590046793; _ga=GA1.2.295735516.1590046793; _gid=GA1.2.2101929115.1590046793; _ym_uid=1590046793649360156; _ym_d=1590046793; _ym_visorc_19426846=b; _ym_isad=2; _fbp=fb.1.1590046793803.466787836; default_ca=1',
        'referer': 'https: // www.kufar.by /',
        'sec - fetch - dest': 'document',
        'sec - fetch - mode': 'navigate',
        'sec - fetch - site': 'same - origin',
        'sec - fetch - user': '?1',
        'upgrade - insecure - requests': '1',
        'user - agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.104',
    }
    resp = se.get(FEED)
sleep(3)

index = BeautifulSoup(resp.content, 'html.parser')
sleep(3)


def start():
    x = 0
    for el in index.select('a'):
        if x < 10:
            x1 = el.get('href')
            x2 = el.find('h3')
            if 'item' in x1 and x2.text:
                x += 1
                x3 = x2.text + ' -- ' + x1
                try:
                    bot.send_message(CHANNEL, x3, parse_mode='Markdown')
                except:
                    pass
        else:
            break


@bot.message_handler(commands=['start'])
def start_command(CHANNEL):
    start()


bot.polling(none_stop=True, interval=0)

if '__main__' == 'kufar':
    start_command()
