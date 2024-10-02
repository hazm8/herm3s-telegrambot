import sys
import os
import telebot
import json
import time
import requests
from auto11 import auto_gen
from lamachat import get_ollama_response
from lamachat import get_sez_response
import secret as secret

#Import Token Keys
TOKEN = secret.TOKEN
CHAT_ID = secret.CHAT_ID

## Initialise the TeleBot
bot = telebot.TeleBot(TOKEN)


#Ollama Live Bot > Responds to all commands
@bot.message_handler(func=lambda message: True)
def handle_ollama_command(message):
    prompt = message.text  # You can modify this to take user input
    response = get_sez_response(prompt, model = 'hermes3', user_chat=message.text)

    # Send the response back to the user in Telegram
    bot.reply_to(message, response)
    pic = auto_gen(response, message.text)
    with open(pic, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

                #bot.send_photo(CHAT_ID, photo=pic)

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(none_stop=True)
