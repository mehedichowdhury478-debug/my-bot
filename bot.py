import os
import threading
from flask import Flask
from pyrogram import Client, filters

web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(
        "👋 Welcome!\n\n"
        "এটা শুধু test bot.\n"
        "Render + GitHub দিয়ে চলছে ✅"
    )

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    app.run()
