import discord
import os
from KeepAlive import keep_alive
import random
import json
import requests
from neuralintents import GenericAssistant

chatbot = GenericAssistant("intents.json")
chatbot.train_model()
chatbot.save_model()

client = discord.Client()
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']


# random_letter = random.choice(abc)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("What's popping?"):
        await message.channel.send("Don't mind me, just watching.")

    if message.content.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.channel.id == 914311577996509265:
        response = chatbot.request(message.content)
        await message.channel.send(response)



    if message.content.startswith("!help"):
        await message.channel.send(
            "Hello! This bot is mainly for automatically responding to messages. It responds to 'What's popping?', "
            "'Big brain', 'Imposter', words that are emojis, and mentions of names in the server. Here is some commands I can do: "
            "!wordfight - A game that whoever types a random letter first wins. \n"
            "!inspire - Get some inspiration from quotes. \n"
            "!help - Get information about this bot, this command.\n"
            "This bot also has a chat bot feature if you type in the botchat channel which uses AI to recognize things like greetings and respond accordingly.")

    if message.content.startswith("!wordfight"):
        # victim = message.content.split("!wordfight ", 0) [0]
        # attacker = '{0.author.mention}'.format(message)
        channel = message.channel

        def check(m):
            #  if message.author != victim or attacker:
            #   await message.channel.send("Stop")
            #  return False

            return m.content == random_letter and m.channel == channel

        # vna = ''+victim+' '+attacker
        random_letter = random.choice(abc)
        await message.channel.send('First person to say ' + random_letter + ' wins!')
        msg = await client.wait_for('message', check=check)
        await message.channel.send('{.author} is the winner!'.format(msg))
        # msg = await client.wait_for('message', )
        # if msg == random_letter:
        # await message.channel.send('Winner!')

    if 'BIG BRAIN' in message.content.upper():
        await message.channel.send("Did someone say big brain?")
    if any([keyword in message.content.upper() for keyword in ('BENJAMIN', 'REDLAZER')]):
        await message.channel.send("Did someone say something about redlazer? <@688491345131601964>")

    if any([keyword in message.content.upper() for keyword in ('EVAN', 'MAGGSDOG')]):
        await message.channel.send("Did someone say something about MaggsDog? <@803419086838169620>")

    if any([keyword in message.content.upper() for keyword in ('JONATHAN', 'DIHYDROGENMONOXIDE')]):
        await message.channel.send("Did someone say something about DihydrogenMonoxide? <@603750653516578848>")

    if any([keyword in message.content.upper() for keyword in ('JOEY', 'WHO WHY ARE YOU')]):
        await message.channel.send("Did someone say something about who why are you? <@803420542707040306>")
    if any([keyword in message.content.upper() for keyword in ('IMPOSTER', 'SUS')]):
        await message.channel.send("sus sus sus amogus reference?")
    if 'POOP' in message.content.upper():
        await message.channel.send(":poop:")
    if any([keyword in message.content.upper() for keyword in ('SOPHISTICATED', 'FANCY', 'MYSTERY')]):
        await message.channel.send(":face_with_monocle:")
    if 'SURE' in message.content.upper():
        await message.channel.send(":face_with_raised_eyebrow:")


keep_alive()
#TOKEN = 
client.run(TOKEN)