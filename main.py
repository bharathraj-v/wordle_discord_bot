import os
import random
import discord
from dotenv import load_dotenv
from keep_alive import keep_alive
word_list = ["comet","jaunt","enema","steed","abyss","growl","fling","dozen","boozy","erode","world","gouge","click",
"briar","great","altar","pulpy","blurt","coast","duchy","groin","fixer","group","rogue","badly","smart","pithy","gaudy","chill",
"heron","vodka","finer","surer","radio","rouge","perch","retch","wrote","clock","tilde","store","prove",
"bring","solve","cheat","grime","exult","usher","epoch","triad","break","rhino","viral","conic","masse","sonic","vital","trace",
"using","peach","champ","baton","brake","pluck","craze","gripe","weary","picky","acute","ferry","aside","tapir","troll","unify",
"rebus","boost","truss","siege","tiger","banal","slump","crank","gorge","query","drink","favor","abbey","tangy","panic","solar",
"shire","proxy","point","robot","prick","wince","crimp","knoll","sugar","whack","mount","perky","could","wrung","light","those","moist","shard",
"pleat","aloft","skill","elder","frame","humor","pause","ulcer","ultra","robin","cynic","agora","aroma","caulk","shake","pupal","dodge","swill",
"tacit","other","thorn","trove","bloke","vivid","spill","chant","choke","rupee","nasty","mourn","ahead","brine","cloth","hoard","sweet","month",
"lapse","watch","today","focus","smelt","tease","cater","movie","lynch","saute","allow","renew","their","slosh","purge","chest","depot","epoxy",
"nymph","found","shall","harry","stove","lowly","snout","trope","fewer","shawl","natal",
"fibre","comma","foray","scare","stair","black","squad","royal","chunk","mince","slave","shame",
"cheek","ample","flair","foyer","cargo","oxide","plant","olive","inert"]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='$word help', url='https://github.com/bharathraj-v/'))

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

    if message.content.startswith('$word help'):
        await message.channel.send("Type $start to start playing\nGreen Square means that the letter is in correct position.\nYellow means that the letter "+
                                    "not in the right position.\nRed means that the letter does not exist.\n\nType $about for more info")
    if message.content.startswith('$about'):
        await message.channel.send("This discord bot is inspired by Wordle, a simple game that took the internet by storm. This is a discord bot implementation "+
                                "that I thought would be cool to play with friends.")

    if message.content.startswith('$start'):
        await message.channel.send("Start guessing a 5 letter word beginning with $guess. for example, $guess cable")
        global word
        word = random.choice(word_list)
        global count
        count = 0
        print(word)

    if message.content.startswith('$guess'):
        guess = message.content.split(' ')[1]
        guess_list = list(guess.lower())
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
                await message.channel.send("The word has been reset. Start guessing again!")
                word = random.choice(word_list)
                count = 0
                print(word)




keep_alive()

client.run(TOKEN)
