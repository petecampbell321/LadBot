import discord
import os
import requests
import json

client = discord.Client()

def get_advice():
  response = requests.get("	https://api.adviceslip.com/advice")
  print(response)
  json_data = json.loads(response.text)
  advice = json_data['slip']['advice']
  print('Sent: ' + advice)
  return advice

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$hello'):
    await message.channel.send('Hello!')

  if msg.startswith('$advice'):
    advice = get_advice()
    await message.channel.send(advice)

  if msg.startswith('you\'re a'):
    await message.channel.send('No u.')

# BOT IDEAS
# - Trivia bets (using https://opentdb.com/api_config.php)

client.run(os.getenv('TOKEN'))