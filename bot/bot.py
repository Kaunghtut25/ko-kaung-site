#!/usr/bin/env python3
"""Ko Kaung Telegram Bot — runs 24/7 on PythonAnywhere (free tier)"""

import os
import requests
import time

# === CONFIG ===
TOKEN = os.environ.get("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")
API = f"https://api.telegram.org/bot{TOKEN}"

def send_message(chat_id, text):
    try:
        requests.post(f"{API}/sendMessage", json={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML"
        }, timeout=10)
    except Exception as e:
        print(f"Send error: {e}")


def handle_update(update):
    msg = update.get("message", {})
    text = msg.get("text", "")
    chat_id = msg.get("chat", {}).get("id")

    if not chat_id:
        return

    if text.startswith("/start"):
        name = msg.get("from", {}).get("first_name", "there")
        send_message(chat_id, f"Hey {name}! I'm Ko Kaung's bot. 🤖\n\n"
                              f"/about - About me\n"
                              f"/ping - Check if I'm alive\n"
                              f"/help - Show commands")

    elif text.startswith("/about"):
        send_message(chat_id, "👤 <b>Ko Kaung</b>\n"
                              "Developer from Myanmar 🇲🇲\n"
                              "GitHub: github.com/Kaunghtut25")

    elif text.startswith("/ping"):
        send_message(chat_id, "🏓 Pong! I'm alive.")

    elif text.startswith("/help"):
        send_message(chat_id, "Commands:\n"
                              "/start - Welcome\n"
                              "/about - About me\n"
                              "/ping - Check status\n"
                              "/help - This list")

    else:
        send_message(chat_id, "Sorry, I only understand commands.\n"
                              "Try /help to see what I can do.")


def poll():
    offset = 0
    while True:
        try:
            resp = requests.get(f"{API}/getUpdates", params={
                "offset": offset,
                "timeout": 30
            }, timeout=35)

            if resp.status_code == 200:
                updates = resp.json().get("result", [])
                for update in updates:
                    handle_update(update)
                    offset = update["update_id"] + 1
            else:
                print(f"API error: {resp.status_code} {resp.text}")

        except requests.RequestException as e:
            print(f"Poll error: {e}")
            time.sleep(5)


if __name__ == "__main__":
    if "YOUR" in TOKEN:
        print("⚠️  Set BOT_TOKEN environment variable!")
        print("   1. Message @BotFather on Telegram to create a bot")
        print("   2. Copy the token")
        print("   3. Run: BOT_TOKEN=your_token python3 bot.py")
    else:
        print("🤖 Bot is running...")
        poll()
