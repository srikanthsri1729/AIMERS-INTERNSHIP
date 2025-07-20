import os
import telebot
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Load env vars from .env file

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

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
)

chat_session = model.start_chat(history=[])

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Welcome! SrikanthPata AI Powerful BOT, Ask your questions related to Anything"
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = chat_session.send_message(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")


from keep_alive import keep_alive
from threading import Thread

def run_bot():
    bot.polling()

# Start bot in background thread
bot_thread = Thread(target=run_bot)
bot_thread.daemon = True
bot_thread.start()

# Keep Flask server as main process
keep_alive()
