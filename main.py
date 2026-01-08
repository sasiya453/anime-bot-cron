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
]

# List of "Hot" Emojis
HOT_EMOJIS = ["🔥", "🍑", "💦", "🥵", "💋", "🌶️", "😈", "👅", "🤤"]
# =========================================

def build_message():
    # Selects 2 random emojis from the list (can include duplicates like 🔥🔥)
    # k=2 means pick 2 items
    picks = random.choices(HOT_EMOJIS, k=2)
    return "".join(picks)

async def main():
    if not API_ID or not API_HASH or not SESSION_STRING:
        print("Error: Missing Secrets (API_ID, API_HASH, or SESSION_STRING).")
        return

    # Random delay before starting
    delay = random.randint(10, 60)
    print(f"Sleeping for {delay} seconds before sending...")
    await asyncio.sleep(delay)

    print("Connecting to Telegram...")
    # Initialize the client with the session string
    async with TelegramClient(StringSession(SESSION_STRING), int(API_ID), API_HASH) as client:
        for chat_id in GROUP_IDS:
            msg = build_message() # Generates the 2 emoji combo
            try:
                # Send message as YOU
                await client.send_message(chat_id, msg)
                print(f"[OK] Sent '{msg}' to {chat_id}")
            except Exception as e:
                print(f"[ERROR] Could not send to {chat_id}: {e}")
            
            # Small pause between groups to avoid flood wait errors
            await asyncio.sleep(random.randint(5, 20))

if __name__ == "__main__":
    # Telethon is async, so we run it inside an event loop
    asyncio.run(main())
