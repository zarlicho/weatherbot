import telebot
from telebot import types
import requests
url = 'https://wttr.in/'
api = '5479340052:AAFvwOVGJgRDa8sLIJy6yjolkv5O4I4yPOs'
bot = telebot.TeleBot(api)
url3 = 'https://v3.wttr.in/'
link = 'https://v2.wttr.in/'
 
@bot.message_handler(commands=['start', 'help', 'about'])
def send_welcome(message):
 bot.send_message(message.chat.id, 'hello this is a weather checker bot, to start you can type /weather city name')
@bot.message_handler(commands=['weather']) 
def echo_message(message):
    try:
        pesan = message.text
        bagi = pesan.split(' ',1)
        search = bagi[1]
        # untuk links
        url1 = (url + search)  # input url
        url2 = (url + search + ".png")
        url4 = (url3 + search + ".png")
        link1 = (link + search + ".png")
        mg = requests.get(url2)
        maps = requests.get(url4)
        bot.send_message(message.chat.id, url2)
        #bot.send_message(message.chat.id, url4)
        bot.send_message(message.chat.id, link1)
        one = requests.get(url1+"?format=4")
        specified = requests.get(url1+"?format=%l+%c+%p+%C")
        add = requests.get(url1+"?format=Preasure:+%P_\nHumidity:+%h+\nTemp:%t")
        bot.send_message(message.chat.id, "location\n"+one.text+"\nspecified\n"+specified.text+"\nsuhu\n"+add.text+"\n"+url4)
    except:
        pass
 
 
print('bot start running')
bot.polling()