import discord
import os
import requests
import json
from keep_alive import keep_alive
from my_openai import ai_response

# BOT IDEAS
# - Trivia bets (using https://opentdb.com/api_config.php)
# - Score system (Like gems in work Slack)
# - GPT-3

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

  if msg.startswith(''):
    await message.channel.send(ai_response(msg))

keep_alive()
client.run(os.getenv('TOKEN'))