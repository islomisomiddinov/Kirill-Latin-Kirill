#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 11:41:53 2025

@author: islomisomiddinov
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '7645543519:AAHg2ilm78-JRjck8b9gQLwmTGipy8kYMKQ'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalom aleykum, Xush kelibsiz!"
    javob += "\nMatn kiriting: "
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinity_polling()

# print(to_latin('дастур'))

# matn = input("Matn kiriting:")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))