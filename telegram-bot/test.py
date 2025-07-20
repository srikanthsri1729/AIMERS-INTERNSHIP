TelegramBOT_TOKEN = 'place your Telegram bot token here ' #Replace wth your TelegramBOT_TOKEN 

#general

#Latest version #Gemini API #AIMER Society #IndianServers
import telebot
import os


"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key="place your gemini api key here") #Replace with your Gemini api key

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)


bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! SrikanthPata AI Powerful BOT, Ask your questions related to Anything")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
 try :
  print(message)
  response=chat_session.send_message(message.text)
  bot.reply_to(message, response.text)

 except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()
