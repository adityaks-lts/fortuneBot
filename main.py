import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()

ask_words = ['?','kya','Kya','did','Did']

def get_quotea():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quotes = json_data[0]['q'] + " -" + json_data[0]['a'] 
  return(quotes)
http://one.airtel.in/
def addingReply(replyedMessage):
  db['rand_reply'] = db["rand_reply"] + "," + replyedMessage


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))




@client.event
async def on_message(message):
  db['rand_reply'] = "Yes,No,I don't know"
  rand_reply = db['rand_reply'].split(',')

  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  
  if message.content.startswith('$inspire'):
    await message.channel.send(get_quotea())
  
  if any(word in message.content for word in ask_words) :
    await message.channel.send(random.choice(rand_reply))
  
  if message.content.startswith('$addre_'):
    replyedMessage = message.content[7:]
    addingReply(replyedMessage)
    await message.channel.send('New reply is added to your list')
  
  if message.content.startswith("$RPS"):
    await message.channel.send('\nLets play....')
    await message.channel.send('\nRock, Paper, Scissors Shoot')
  
  if message.content.startswith("Rock") or message.content.startswith("Paper") or message.content.startswith("Scissors"):
    elements = ['Rock', 'Paper', 'Scissors']
    player = message.content
    computer = random.choice(elements) 
    await message.channel.send("I got "+computer)
    await message.channel.send("Your got "+player)
#Rules
    if computer == "Rock" and player =="Scissors":
      await message.channel.send("I win")
    if computer == "Scissors" and player == "Paper":
      await message.channel.send("I win")
    if computer == "Paper" and player == "Rock":
      await message.channel.send("I win")
    if computer == "Rock" and player == "Paper":
      await message.channel.send("You win")
    if computer == "Scissors" and player == "Rock":
      await message.channel.send("You win")
    if computer == "Paper" and player == "Scissors":
      await message.channel.send("You win")
    if computer == player:
      await message.channel.send("Oho We got tie")

keep_alive()
client.run(os.getenv('TOKEN'))
