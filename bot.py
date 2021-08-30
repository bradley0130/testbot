import discord
import os
import requests
import json
import random

client = discord.Client()

bad_words = ["fuck", "shit"]

stop = [
  "Don't say that!",
  "You should die now!",
  "KYS bitch",
  "Die in the shitter and kys in #general chat"
]

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

    msg = message.content

    if msg.startswith('.inspire'):
      quote = get_quote()
      await message.channel.send(quote)

    if msg.startswith('.help'):
      await message.channel.send('Commands **.help** **.test** **.inspire** **.update** if you say fuck or shit you get a cool message and **.info**')

    if msg.startswith('.info'):
      await message.channel.send('Im made in Python and you can find all my code here: https://github.com/bradley0130/testbot')
      
    if msg.startswith('.test'):
      await message.channel.send('Fuck off, bitch!')
    
    if msg.startswith('.update'):
      await message.channel.send('I no longer have a use bradley will stop updating me on replit and find another way to make discord bots. Until then this is the last update for this bot')
    
    if any(word in msg for word in bad_words):
      await message.channel.send(random.choice(stop))

my_secret = os.environ['TOKEN']

client.run(os.getenv('TOKEN'))
