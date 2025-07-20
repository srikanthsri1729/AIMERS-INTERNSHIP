# AIMERS-INTERNSHIP

#TELEGRAM BOT:

   # 🤖 AI-Powered Telegram Bot using Gemini API

A smart Telegram bot that uses Google's Gemini API to respond to user messages in real time — built in Python, developed in Google Colab, and deployed on Replit for 24/7 uptime.

---

## 🚀 Features
- Real-time chatbot responses powered by **Google Gemini**
- Telegram Bot API integration
- Deployed on Replit with UptimeRobot to keep it running 24/7
- Secure key management using .env

---

## 🛠️ Technologies Used
- Python
- Google Generative AI SDK (gemini-1.5-flash)
- Telegram Bot API (pyTelegramBotAPI)
- Replit (for hosting)
- UptimeRobot (to prevent Replit from sleeping)
- Flask (keep_alive.py) to keep the service alive

---

## 📦 Setup & Deployment
bash
1. Clone the repository
git clone https://github.com/srikanthsri1729/AIMERS-INTERNSHIP.git
cd AIMERS-INTERNSHIP/telegram-bot

##  Install requirements
bash
pip install -r requirements.txt
##  Create a .env file
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_google_gemini_api_key
4. Run the bot
bash
Copy
Edit
python main.py
