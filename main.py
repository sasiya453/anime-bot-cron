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

# List of Group IDs
GROUP_IDS = [
    -1002932620190,
    -1001277604895,
    -1001222853489,
    -1001764420368,
    -1002811254612,
    -1001806767670,
    -1003694840892,
    -1002016551300,
    -1001278896430,
    -1001589174259,
    -1002106770352,
]

# Variations of the message to avoid spam detection
MESSAGE_VARIANTS = [
    "8 Million+ anime artworks 🌸📥",
    "✨ 8 Million+ anime artworks 🌸📥",
    "**8 Million+ anime artworks** 🌸📥",
    "8 Million+ anime artworks 🌸📥 🔥",
    "🌸 8 Million+ anime artworks 📥",
    "__8 Million+ anime artworks__ 🌸📥",
    "⚡ 8 Million+ anime artworks 🌸📥",
    "8 Million+ anime artworks 🌸📥 ✨",
]
# =========================================

def build_message():
    # Pick one random variation from the list
    return random.choice(MESSAGE_VARIANTS)

async def main():
    if not API_ID or not API_HASH or not SESSION_STRING:
        print("Error: Missing Secrets (API_ID, API_HASH, or SESSION_STRING).")
        return

    # Random delay (10 to 60 seconds) to fit within the 5-minute workflow timeout
    delay = random.randint(10, 60)
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
                print(f"[OK] Sent '{msg}' to {chat_id}")
            except Exception as e:
                print(f"[ERROR] Could not send to {chat_id}: {e}")
            
            # Small pause between groups to avoid flood wait errors
            await asyncio.sleep(random.randint(5, 20))

if __name__ == "__main__":
    asyncio.run(main())
