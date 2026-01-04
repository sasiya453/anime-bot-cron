import time
import random
import requests
import os

# ================ CONFIG =================
# We get the token from GitHub Secrets for security
BOT_TOKEN = os.environ.get("BOT_TOKEN")

GROUP_IDS = [
    -1003694840892,
]

BASE_MESSAGE = "👀🔞 (adult only)\n\nExplore 8M+ anime artworks\n\nCheck Bio & Start"

EXTRA_EMOJI_VARIANTS = [" 🌸", " 🌸✨", " 🌸💮", " 🌸💗", " 🌸🔥", " 🌸💦", " 🌸🍑"]

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
# =========================================

def build_message():
    extra = random.choice(EXTRA_EMOJI_VARIANTS)
    return BASE_MESSAGE + extra

def send_message(chat_id, text):
    payload = {"chat_id": chat_id, "text": text}
    try:
        response = requests.post(API_URL, data=payload, timeout=10)
    except Exception as e:
        print(f"[ERROR] {chat_id}: {e}")
        return False
    
    if not response.ok:
        print(f"[ERROR] {chat_id}: {response.text}")
        return False
    print(f"[OK] Sent to {chat_id}")
    return True

def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN not found.")
        return

    # Random delay between 0 and 60 minutes to vary the time
    # This simulates the "4 to 5 hours" window when combined with a 4-hour schedule
    delay = random.randint(60, 600)
    print(f"Sleeping for {delay} seconds before sending...")
    time.sleep(delay)

    for chat_id in GROUP_IDS:
        msg = build_message()
        send_message(chat_id, msg)
        # Small pause between groups
        time.sleep(random.randint(5, 20))

if __name__ == "__main__":
    main()
