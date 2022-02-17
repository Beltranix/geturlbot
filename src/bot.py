from pyrogram import Client, filters
from bot_functions import Functions

API_ID = 
API_HASH = ""
BOT_TOKEN = ""

app = Client("my_account", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
f = Functions()

@app.on_message(filters.regex(r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'))
def echo(client, message):
    message.reply(f.get_streamlink(message.text))

app.run()
