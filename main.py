from itertools import count
import os
import random
import discord
from dotenv import load_dotenv

word_list = ["humph","delve","growl","agora","ahead","augur","hyper","homer","cramp", "whelp", "bleed","asset",
"fella","delve","unfit","movie","alike","scare","smear","alpha","crimp","altar","hunky","labor","bleed","leave",
"groin","ruder","spill","crate","loopy","error","liver","wench","vigor","motto","being","admit","bluff","drink",
"chest","group","delve","stool","offal","vouch","liver","evade","first","gripe","goose","store","crate","banal",
"jaunt","fibre","round","spend","panel","pound","fibre","alien","biome","cheek","flock","stead","smear","pinto",
"stomp","admit","purge","wince","elder","ultra","roomy","argue","trice","sever"]


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='$help', url='https://github.com/bharathraj-v/'))

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event

async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send("Type $start to start playing\nGreen Square means that the letter is in correct position.\nYellow means that the letter "+
                                    "not in the right position.\nRed means that the letter does not exist.\n\nType $about for more info")
    if message.content.startswith('$about'):
        await message.channel.send("This discord bot is inspired by Wordle, a simple game that took the internet by storm. This is a discord bot implementation "+
                                "that I thought would be cool to play with friends. Better versions of this bot exist on the internet but this was a good project "+
                                "to work on for fun.")

    if message.content.startswith('$start'):
        await message.channel.send("Start guessing a 5 letter word beginning with $guess. for example, $guess cable")
        global word
        word = random.choice(word_list)
        global count
        count = 0
        print(word)

    if message.content.startswith('$guess'):
        guess = message.content.split(' ')[1]
        guess_list = list(guess)
        if len(guess)!= 5:
            await message.channel.send("Please guess a 5 letter word!")
        if len(guess)==5:
            result = ''
            for i in range(len(guess_list)):
                if guess_list[i] not in list(word):
                    result += " :red_square:"
                    count+=1
                elif (guess_list[i] in list(word)) and (word[i]!=guess_list[i]):
                    result += " :yellow_square:"
                    count+=1
                elif word[i]==guess_list[i]:
                    result += " :green_square:"
                    count+=1
            await message.channel.send(result+"     "+" Tries: "+str(int(count/5)))
            if result == " :green_square:"*5:
                await message.channel.send("Congratulations. You have got the word in "+str(int(count/5))+" tries")
                await message.channel.send("Type $start to reset the word and start playing again!")




client.run(TOKEN)
