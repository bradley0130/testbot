import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('.inspire'):
      quote = get_quote()
      await message.channel.send(quote)

    if message.content.startswith('.help'):
      await message.channel.send('Commands **.help** **.test** **.inspire** and **.info**')

    if message.contest.startswith('.info'):
      await message.channel.send('Im made in Python and you can find all my code here: https://github.com/bradley0130/testbot')
    if message.content.startswith('.test'):
      await message.channel.send('Fuck off, bitch!')

my_secret = os.environ['TOKEN']

client.run(os.getenv('TOKEN'))
