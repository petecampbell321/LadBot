import os
import openai
# import requests

openai.organisation = "org-GFMpTroBuYhWzDvoXgiWmimp"
openai.api_key = os.getenv("OPENAI_API_KEY")

def engine_list():
  openai.Engine.list()

def ai_response(prompt):
  response = openai.Completion.create(
    engine="curie",
    prompt=prompt
  )
  print(response)
  return response.choices[0].text