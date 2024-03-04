import requests
import json
import discord

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$meme'):
            meme_url = get_meme()
            await message.channel.send(meme_url)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Replace with your own token.') # Replace with your own token.

