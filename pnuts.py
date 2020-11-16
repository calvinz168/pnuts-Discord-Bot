#pnuts
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
#from PIL import Image
import random
import datetime
from datetime import datetime
import requests
import json
import time
#import PyNaCl

client = commands.Bot(command_prefix = "")

global mcGen,pnutGen,calvin1,calvin2,nathan,caleb,adam,marcus,vivian
mcGen = client.get_channel(574067087442575360)
pnutGen = client.get_channel(747530161045504132)
calvin1 = client.get_user(241383496629616641)
calvin2 = client.get_user(749064332872253512)
nathan  = client.get_user(404377415331217408)
caleb   = client.get_user(352300752003137536)
adam    = client.get_user(181920051350339584)
marcus  = client.get_user(510448844052496385)
vivian  = client.get_user(303160967410352129)
caitlin = client.get_user(342841594778615827)
#Channels -----------------------  
#747530161045504132 - pnut test         - general
#747629690638041119 - minecraft bitches - pnuts
#574067087442575360 - minecraft bitches - general


#events -----------------------           
@client.event
async def on_ready():
    global mcGen,pnutGen,calvin1,calvin2,nathan,caleb,adam,marcus,vivian,caitlin
    mcGen = client.get_channel(574067087442575360)
    pnutGen = client.get_channel(747530161045504132)
    calvin1 = client.get_user(241383496629616641)
    calvin2 = client.get_user(749064332872253512)
    nathan  = client.get_user(404377415331217408)
    caleb   = client.get_user(352300752003137536)
    adam    = client.get_user(181920051350339584)
    marcus  = client.get_user(510448844052496385)
    vivian  = client.get_user(303160967410352129)
    caitlin = client.get_user(342841594778615827)
    print("bot is ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="c gang"))

@client.event
async def on_command_error(ctx, error):
     if isinstance(error, commands.CommandNotFound):
        # fails silently, else you get error every time a message received is not a command
        pass

@client.event
async def on_message_error(ctx, error):
    if isinstance(error, commands.forbidden):
        # fails silently, on DM
        pass

#commands ------------------------------
@client.command(aliases = ["Lobster"])
async def lobster(ctx):
    randLob = random.randint(1,50)
    await ctx.send(file=discord.File(f'{randLob}.jpg'))

@client.command(aliases = ["Lobsters"])
async def lobsters(ctx, arg):
    await ctx.send(file=discord.File(f'{arg}.jpg'))

@client.command(aliases = ["Abortion"])
async def abortion(ctx):
    abortionNotes = [f"A 23 year old woman came in 11 months into her pregnancy and said 'I dont want my stupid baby anymore, kill it' and the doctor said 'okay' and he put jumper cables up her baby hole and connected them to a car battery and let it run for six days straight", "A little 8-year old girl wandered in and said 'I want an abortion but I am not pregnant' and the doctor said 'well fix that' and he stole a baby and cut the girl open and put the baby inside her and sewed her shut and then woke the girl up and said 'congratulations its a healthy six year old boy' and the girl said 'can I keep him' and the doctor said no and then backed over her in the parking lot with his brand new Ford Raptor", "One of the doctors there developed a futuristic ray gun that could make anything he shot have an abortion, even trees, cars, or barns", "The doctors assistant invented this thing she called 'the silly slide' and it was a really fun little water slide that connected a womans vagina to a paper shredder so a newborn baby could briefly 'enjoy the high life'", "The oldest child we aborted was in his late 70s, we didn't even know he was a baby until his wife brought in photos", "⁠The doctors put all sorts of crap up a womans uterus including a clown nose, bicycle handlebars, a calendar, and an entire Sears retail outlet (before bankruptcy)", "During every successful abortion, the doctor would shout 'take that, baby' and he would push a red button that made sirens go off and confetti fell from the ceiling and we would all get Del Taco for free"]
    randAbo = random.randint(0,6) 
    await ctx.send(abortionNotes[randAbo])

@client.command(aliases = ["Quote"])
async def quote(ctx):
    quotes = ["Shut yo skin tone chicken bone google chrome no home flip phone disowned ice cream cone garden gnome extra chromosome metronome dimmadome genome full blown monochrome student loan indiana jones overgrown flintstone x and y hormone post malone friend zone sylvester stallone hydrocortisone sierra leone autozone professionally seen silver patrone head ass tf up","Eat trash Get cash Slurp ass Die fast","The final stand is wherever I plant my feet. Not one step more. - Saint 14","Death is only the end if you assume the story is about you","When you watch the birds, they watch you too","Sleep like theres nobody watching","I physically cannot stop myself from saying 'bruh moment' whenever i react to anything. What was originally a rather humorous saying has evolved to now an impulsive, uncontrollable behavior that consumes me whenever i have to react to something. From 'holy crap' and omg to 'bruh' all that is said now is 'bruh moment'. 'bruh moment' this 'bruh moment'. my family died. bruh moment. im having the time of my life. bruh moment. i just wanted to be cool and say something original. bruh moment. little did i know the horrors that came from bruh moment. im doomed. bruh moment. this phrase has gotten the best of me. its over for me. bruh moment. bruh sound effect. b r u h m o m e n t. bruh.", "If you’re not dying you’re not living", "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.", "Real gangsta ass niggas dont have to flex nuts, cause real gangsta ass niggas know they got them  -Socrates", "When i raise this sword, so i wish that this poor sinner will receive eternal life.", "When there is no more room in hell, the dead will walk the earth", "Ask the rice for he knows all. But not right now hes busy", "Jeez louise i crave the cheese", "Tell me the name of god you fungal piece of shit", "Too dead to die", "Every second you’re not running, Im only getting closer", "Danger is my bread, and death; my butter", "When tyranny becomes law, resistance becomes duty", "Only dead fish go with the flow", "Cum is stored in the brain, and i have a headache", "If thou gaze long into an abyss, the abyss will also gaze into thee", "Forecast: making it rain", "If a man does not have the sauce,then he is lost. But the same man can be lost in the sauce", "live every day like its your last before you die from a a drive-by crossbow shot at 8:39 tomorrow", "Stand in the ashes of a trillion dead souls and ask the ghosts if honor really matters", "Be polite. Be courteous. Show professionalism and have a plan to kill everyone in the room", "my demons are chasing me and they’re doing the naruto run", "Money doesn’t change people, it unlocks characters which were jailed by poverty", "My crocs have holes so my swag can breathe", "aloha my broha", "Spend fiddies, pet kitties, suck tiddies", "when you’re in hell, only the devil can save you","the blood of the covenant is thicker than the water of the womb","how fleeting are all human passions compared with the massive continuity of ducks","Once you've read the dictionary, every other book you read is just a remix"]
    randQuo = random.randint(0,34)
    await ctx.send(quotes[randQuo])

@client.command(aliases = ["Sploch"])
async def sploch(ctx):
    await ctx.send("You ever just sploch on a homie")

@client.command(aliases = ["Fallacy"])
async def fallacy(ctx):
    emb = discord.Embed(title="When your homie tells you that their minecraft playing cousin is a 12 year old chinese person, and they really aint - Vovian Ren")
    await ctx.send(embed=emb)

@client.command(aliases = ["Remind"])
async def remind(ctx):
    await ctx.send("3. New fucking rule, if you say @ everyone nibba I'm literally gonna revoke your perms")

@client.command(aliases = ["Robust"])
async def robust(ctx):
    await ctx.send("No more Mrs. Nice Quesnelle")

@client.command(aliases = ["Grape","grapes","Grapes"])
async def grape(ctx):
    await ctx.message.add_reaction("🍇")
    
#math -----------------------  
@client.command(aliases = ["Add"])
async def add(ctx, arg, arg2):
    sum = int(arg) + int(arg2)
    return await ctx.send(f'{arg} + {arg2} is: {sum}')

@client.command(aliases = ["Subtract"])
async def subtract(ctx, arg, arg2):
    sum = int(arg) - int(arg2)
    return await ctx.send(f'{arg} - {arg2} is: {sum}')

@client.command(aliases = ["Multiply"])
async def multiply(ctx, arg, arg2,):
    product = int(arg) * int(arg2)
    return await ctx.send(f'{arg} * {arg2} is: {product}')

@client.command(aliases = ["Divide"])
async def divide(ctx, arg, arg2,):
    quotient = float(arg) / float(arg2)
    return await ctx.send(f'{arg} / {arg2} is: {quotient}')

#pics -----------------------  
@client.command(aliases = ["Pic","PIC","Picture","picture"])
async def pic(ctx,arg):
    arg = arg.lower()
    picMat = [["josh",11],["adam",12],["marcus",5],["calvin",12],["vivian",11],["caleb",15],["caitlin",5],["hannah",2]]
    for i in range(0,len(picMat)):
        if arg == picMat[i][0]:
            rand = random.randint(1,picMat[i][1])
            return await ctx.send(file=discord.File(f'{picMat[i][0]}{rand}.png'))

@client.command(aliases = ["Logan"])
async def logan(ctx):
    randLog = random.randint(100,107)
    return await ctx.send(file=discord.File(f'{randLog}.jpg'))

#utility commands -----------------------   
@client.command()
async def weather(ctx):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = "Oakville"
    api_key = "fe0c0c0b7ed26a50c489d78880ae5769"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url) 
    x = response.json()
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"]  

        tempCel = round(int(y["temp"]) - 273.13)
        await ctx.send(f"Displaying weather for {city_name}:")
        await ctx.send(f"Current temperature is: {tempCel}")
        await ctx.send(f"Current pressure is: {y['pressure']} hPa")
        await ctx.send(f"Current humidity is: {y['humidity']} %")
        await ctx.send(f"Current weather is: {z[0]['description']}")
    else:
        print(" City Not Found ")
        
@client.command()
async def d(ctx):
    if ((ctx.author == client.get_user(241383496629616641)) or ((ctx.author == client.get_user(749064332872253512)))):
        await ctx.message.delete()
        msg = ctx.message.content
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]
        return await ctx.send(content=f"**{text}**")

@client.command(aliases =["Time"])
async def time(ctx):
    tim = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return await ctx.send(tim)

@client.command(aliases = ["Map","MAP","mAP","MaP"])
async def map(ctx):
    return await ctx.send(random.randint(1,31))

@client.command(aliases = ["Ping"])
async def ping(ctx,user:discord.Member,arg):
    try:
        for i in range(0,int(arg)):
            #a = i + user.mention
            print("ASD")
            await ctx.send(user.mention)
    except:
        await ctx.send("Wrong")
        
@client.command(aliases = ["8ball", "eightBall"])
async def eightball(ctx):
    rand8 = random.randint(0,9)
    rand8List = ["It is certain", "It is decidedly so", "Without a doubt", "As I see it, yes", "Most likely", "Outlook good", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Dont count on it","My reply is no", "My sources say "]
    return await ctx.send(rand8List[rand8])

@client.command(aliases = ["Vote"])
async def vote(ctx):
    randVote=random.randint(1,2)
    if randVote == 1:
        await ctx.send("no")
    else:
        await ctx.send("yes")

@client.event
async def on_message(ctx):
    tim = datetime.now().strftime('%H:%M:%S')
    nathan = client.get_user(404377415331217408)
    randNumba = random.randint(1,1000)
    groovy = client.get_user(234395307759108106)
    tiananmen = ["June 4 1989","june 4 1989","june 4th 1989","June 4th 1989","06 04 1989"
                 ,"June 4, 1989","june 4, 1989","1989 June 4","1989 june 4","1989 4 June"
                 ,"1989 4 june","06/04/89","06/04/1989","j u n e  4  1 9 8 9","the fourth of june 1989"]
    cgang = ["c gang","C gang","grapes","grape"]
    
    print("\n")
    print("Message-------------------------")
    print(f"Author: ",ctx.author)
    print("Message:",ctx.content)
    if ctx.author == vivian:
        await ctx.channel.send("shut up nerd")
        await ctx.delete()
        
    if ctx.content in tiananmen:
        await ctx.channel.send("shhh")
        await ctx.delete()

    if (ctx.content in cgang) and (ctx.author != client.user):
        await ctx.add_reaction("🍇")

    #1/1000 chance for hannah or reminder
    if ctx.author != client.user and randNumba == 999:
        await ctx.channel.send(file=discord.File("hannah2.png"))
    elif ctx.author != client.user and randNumba == 2:
        await ctx.channel.send("3. New fucking rule, if you say @ everyone I'm literally gonna revoke your perms")
    elif ctx.author != client.user and ctx.author != groovy:
        pnuts = client.get_channel(747629690638041119)
        await client.process_commands(ctx)
    #await client.process_commands(ctx)
    
client.run("TOKEN")

