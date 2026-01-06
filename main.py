import time
import random
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# ================ CONFIG =================
# Secrets from GitHub
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

# List of Group IDs or Usernames
# Note: For user accounts, it's safer to use integers (chat IDs) 
# or usernames (e.g., "mygroupname") if you have joined them.
GROUP_IDS = [
    -1003694840892,
]

BASE_MESSAGE = "👀 \n\nExplore 8M+ anime artworks\n\nCheck Bio & Start"

EXTRA_EMOJI_VARIANTS = [" 🌸", " 🌸✨", " 🌸💮", " 🌸💗", " 🌸🔥", " 🌸💦", " 🌸🍑"]
# =========================================

def build_message():
    extra = random.choice(EXTRA_EMOJI_VARIANTS)
    return BASE_MESSAGE + extra

async def main():
    if not API_ID or not API_HASH or not SESSION_STRING:
        print("Error: Missing Secrets (API_ID, API_HASH, or SESSION_STRING).")
        return

    # Random delay (Keep your original logic)
    delay = random.randint(60, 600)
    print(f"Sleeping for {delay} seconds before sending...")
    time.sleep(delay)

    print("Connecting to Telegram...")
    # Initialize the client with the session string
    async with TelegramClient(StringSession(SESSION_STRING), int(API_ID), API_HASH) as client:
        for chat_id in GROUP_IDS:
            msg = build_message()
            try:
                # Send message as YOU
                await client.send_message(chat_id, msg)
                print(f"[OK] Sent to {chat_id}")
            except Exception as e:
                print(f"[ERROR] Could not send to {chat_id}: {e}")
            
            # Small pause between groups to avoid flood wait errors
            await asyncio.sleep(random.randint(5, 20))

if __name__ == "__main__":
    # Telethon is async, so we run it inside an event loop
    asyncio.run(main())
