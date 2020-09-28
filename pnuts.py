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

global mcGen,pnutGen,calvin1,nathan,caleb,adam,marcus,vivian

#Channels -----------------------  
#747530161045504132 - pnut test         - general
#747629690638041119 - minecraft bitches - pnuts
#574067087442575360 - minecraft bitches - general


#events -----------------------           
@client.event
async def on_ready():
    global mcGen,pnutGen,calvin1,nathan,caleb,adam,marcus,vivian
    mcGen = client.get_channel(574067087442575360)
    pnutGen = client.get_channel(747530161045504132)
    calvin1 = client.get_user(241383496629616641)
    calvin2 = client.get_user(749064332872253512)
    nathan  = client.get_user(404377415331217408)
    caleb   = client.get_user(352300752003137536)
    adam    = client.get_user(181920051350339584)
    marcus  = client.get_user(510448844052496385)
    vivian  = client.get_user(303160967410352129)
   # await channel.edit(topic="Ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="c gang"))
    print("Bot is ready")

@client.event
async def on_disconnect():
    mcGen = client.get_channel(747629690638041119)
    await mcGen.edit(topic="Not Ready")

@client.event
async def on_command_error(ctx, error):
     if isinstance(error, commands.CommandNotFound):  # fails silently
        pass
    
##@client.command(pass_context=True)
##async def join(ctx):
##    print(ctx)
##    #author = ctx.message.author
##    channel = ctx.message.author.voice_channel
##    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voiceChannel
    print(channel)
    #await client.join_voice_channel(channel)

    
@client.event
async def on_member_update(before, after):
    if(str(after) != "nuts#9791"):
        return
    else:
        print("me")
        channel = client.get_channel(747629690638041119)
        await channel.edit(topic="Not Ready")
        print("updated")


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

@client.command(aliases = ["No","NO","Nah","nah","Nope","nope"])
async def no(ctx):
    await ctx.send("yes")

@client.command(aliases = ["Yes", "YES","Yup","yup","Yep","yep"])
async def yes(ctx):
    await ctx.send("no")

    
#math -----------------------  
@client.command(aliases = ["Add"])
async def add(ctx, arg, arg2):
    sum = int(arg) + int(arg2)
    await ctx.send(f'{arg} + {arg2} is: {sum}')

@client.command(aliases = ["Subtract"])
async def subtract(ctx, arg, arg2):
    sum = int(arg) - int(arg2)
    await ctx.send(f'{arg} - {arg2} is: {sum}')

@client.command(aliases = ["Multiply"])
async def multiply(ctx, arg, arg2,):
    product = int(arg) * int(arg2)
    await ctx.send(f'{arg} * {arg2} is: {product}')

@client.command(aliases = ["Divide"])
async def divide(ctx, arg, arg2,):
    quotient = float(arg) / float(arg2)
    await ctx.send(f'{arg} / {arg2} is: {quotient}')
    

#copypasta -----------------------  
##@client.command(aliases = ["Covid", "covid", "Corona", "coronavirus", "Coronavirus"])
##async def corona(ctx):
##    await ctx.send("So it seems you’ve tested positive for the Chinese virus, the so-called Covid NINETEEN, the Corona—nobody knows what to call it, quite frankly. It’s the most amazing thing, no one knew anything about Corona until a few weeks ago.But the moment I heard about it—the Wuhan flu; it’s also the Wuhan, or WuHAAN—that’s a city in China. Many people don’t know that. But the moment I heard about this Chinese flu, I ordered a test. And it’s an amazing test. We do better testing than anywhere in the world. Some say the Germans have the best tests, but they don’t. Our tests are even better.So you’re positive for Corona. And usually “positive” is a positive word—it’s a very good word, frankly. Everybody thinks it’s good, apart from what you hear on the news—which is fake. It’s largely fake. But in medicine, “positive” is not so good. So it’s very confusing. And I’ve always been very clear about that. Some say “positive” is always good, but I’ve never agreed with that.So you’re positive for the Corona. But you’ll be fine. Totally fine. You might think you’re going to die—and everybody does die, eventually. But you’ll be fine. You feel fine, right? You won’t need a ventilator. There are no ventilators—but you won’t need one.How old are you, 55? You won’t need one. Some people need a ventilator, and they’re amazing machines. Did you know the first ventilator was made by Henry Ford? It’s an incredible piece of equipment. But you’ll be fine.The virus gets into your lungs, which is where you breathe. But you have two of them. Some say you have a spare. Some people only have one lung. It’s true. But I don’t talk about spares. I always want both. Given a choice, I want two lungs.So I’ve asked nurse—what’s your name, Nancy?—I’ve asked nurse Nancy to keep you comfortable. And Nancy is one of our finest nurses. I mean, just look at her. Incredible, right? Nancy, you’re really incredible. You’re not afraid of Corona, are you, the Chinese Plague? I didn’t think so. Nancy will bring you whatever you need. And if you start coughing, do that into your elbow, so you don’t make a mess. Okay, you’re doing great. I’ll see you later.")
##
##@client.command(aliases = ["Imagine"])
##async def imagine(ctx):
##    await ctx.send("Imagine being Arnold in that scene and having to be all like 'damn, Jamie Curtis, you fuckin' fine, all sexy with your tight body and horrific androgynous monster face. I would totally have sex with you, both my character and the real me.' when all he really wants to do is fuck another 16 year old in his dressing room. Like seriously imagine having to be Arnold and not only sit in that chair while Jamie Lee Curtis flaunts her disgusting body in front of you, the favorable lighting barely concealing her stretchmarks and leathery skin, and just sit there, take after take, hour after hour, while she perfected that dance. Not only having to tolerate her monstrous fucking visage but her haughty attitude as everyone on set tells her she's STILL GOT IT and DAMN, JAMIE LEE CURTIS LOOKS LIKE THAT?? because they're not the ones who have to sit there and watch her mannish fucking gremlin face contort into types of grimaces you didn't even know existed before that day. You've been fucking nothing but a healthy diet of blondes and supermodels and later alleged rape victims for your ENTIRE CAREER coming straight out of the boonies in Austria. You've never even seen anything this fucking disgusting before, and now you swear you can taste the sweat that's breaking out on her dimpled stomach as she sucks it in to writhe it suggestively at you, smugly assured that you are enjoying the opportunity to get paid to sit there and revel in her 'statuesque (for that is what she calls herself)' beauty, the beauty she worked so hard for with personal trainers in the previous months. And then the director calls for another take, and you know you could kill every single person in this room before the studio security could put you down, but you sit there and endure, because you're fucking Arnold. You're not going to lose your future political career over this. Just bear it. Hide your face and bear it.")
##
##@client.command(aliases = ["Bruh", "BRUH"])
##async def bruh(ctx):
##    await ctx.send("i physically cannot stop myself from saying 'bruh moment' whenever i react to anything. What was originally a rather humorous saying has evolved to now an impulsive, uncontrollable behavior that consumes me whenever i have to react to something. From 'holy crap' and omg to 'bruh' all that is said now is 'bruh moment'. 'bruh moment' this 'bruh moment'. my family died. bruh moment. im having the time of my life. bruh moment. i just wanted to be cool and say something original. bruh moment. little did i know the horrors that came from bruh moment. im doomed. bruh moment. this phrase has gotten the best of me. its over for me. bruh moment. bruh sound effect. b r u h m o m e n t. bruh.")
##
##@client.command(aliases = ['Fuck', 'fuck you', 'Fuck you'])
##async def fuck(ctx):
##    await ctx.send("What the frick frack diddily dack patty wack snick snack crack pack slack mack quarterback crackerjack biofeedback backtrack thumbtack sidetrack tic-tac did you just say")
##@client.command(aliases = ["WAP", "Wap"])
##async def wap(ctx):
##    await ctx.send("I said, certified freak Seven days a week Wet ass pussy Make that pull-out game weak, woo Yeah, yeah, yeah, yeah Yeah, you fucking with some wet ass pussy Bring a bucket and a mop for this wet ass pussy Give me everything you got for this wet ass pussy Beat it up, N***, catch a charge Extra large and extra hard Put this pussy right in your face Swipe your nose like a credit card Hop on top, I wanna ride I do a kegel while it's inside Spit in my mouth, look in my eyes This pussy is wet, come take a dive Tie me up like I'm surprised Let's role play, I wear a disguise I want you to park that big Mack truck Right in this little garage Make it cream, make me scream Out in public, make a scene I don't cook, I don't clean But let me tell you how I got this ring (ayy, ayy) Gobble me, swallow me, drip down inside of me Quick jump out 'fore you let it get inside of me I tell him where to put it, never tell him where I'm 'bout to be I run down on him 'fore I have a nigga running me Talk your shit, bite your lip Ask for a car while you ride that dick (while you ride that dick) You really ain't never gotta fuck him for a thang He already made his mind up 'fore he came Now get your boots and your coat For this wet ass pussy He bought a phone just for pictures Of this wet ass pussy Pay my tuition just to kiss me On this wet ass pussy Now make it rain if you wanna See some wet ass pussy")


#pics -----------------------  
@client.command(aliases = ["Pic","PIC","Picture","picture"])
async def pic(ctx,arg):
    picMat = [["josh",11],["adam",12],["marcus",5],["calvin",12],["vivian",9],["caleb",15],["caitlin",5],["hannah",2]]
    for i in range(0,8):
        if arg == picMat[i][0]:
            rand = random.randint(1,picMat[i][1])
            return await ctx.send(file=discord.File(f'{picMat[i][0]}{rand}.png'))


#utility commands -----------------------  
@client.command()
async def t(ctx):
    global mcGen,pnutGen,calvin1,nathan,caleb,adam,marcus,vivian
    if ctx.author == calvin1 or ctx.author == calvin2:
        await ctx.message.delete()
        print("")
        print("SEND MESSAGE--------------------")
        text = input("Message: ")
        print("") 
        receiverDict={"calvin1":calvin1,"nathan":nathan,"caleb":caleb,"adam":adam,"marcus":marcus,"vivian":vivian,"mcGen":mcGen,"pnutGen":pnutGen}
        for i in receiverDict:
            print(receiverDict[i])
        receiver = input("Receiver: ")
        for i in receiverDict:
            if receiver == i:
                await receiverDict[i].send(text)
                
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
        await ctx.send(f"Current pressure is: {y['pressure']} hpa")
        await ctx.send(f"Current humidity is: {y['humidity']} %")
        await ctx.send(f"Current weather is: {z[0]['description']}")
    else: 
        print(" City Not Found ")
        
@client.command(aliases =["Time"])
async def time(ctx):
    tim = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(tim)

@client.command(aliases = ["Map"])
async def map(ctx):
    return await ctx.send(random.randint(1,31))

@client.command()
async def ping(ctx,user:discord.Member,arg):
    global channel,calvin1,nathan,caleb,adam,marcus,vivian
    if ctx.author != nathan:
        try:
            for i in range(0,int(arg)):
                await ctx.send(user.mention)
        except:
            await ctx.send("Missing argument")
    print(ctx.message)

@client.command(aliases = ["8ball", "eightBall"])
async def eightball(ctx):
    rand8 = random.randint(0,9)
    rand8List = ["It is certain", "It is decidedly so", "Without a doubt", "As I see it, yes", "Most likely", "Outlook good", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Dont count on it","My reply is no", "My sources say "]
    return await ctx.send(rand8List[rand8])

@client.command()
async def mute(ctx, member: discord.Member):
    global mcGen,pnutGen,calvin1,nathan,caleb,adam,marcus,vivian
 
    print("mute")
    if ctx.message.author == calvin1 or ctx.message.author == adam :
        print("ASD")
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)

@client.command(aliases = ["Vote"])
async def vote(ctx):
    randVote=random.randint(1,2)
    if randVote == 1:
        await ctx.send("no")
    else:
        await ctx.send("yes")

@client.event
async def on_message(ctx):
    global channel,calvin1,nathan,caleb,adam,marcus,vivian
    tiananmen = ["June 4 1989","june 4 1989","june 4th 1989","June 4th 1989","06 04 1989"
                 ,"June 4, 1989","june 4, 1989","1989 June 4","1989 june 4","1989 4 June"
                 ,"1989 4 june","06/04/89","06/04/1989","j u n e  4  1 9 8 9","the fourth of june 1989"]
    randNumba = random.randint(1,1000)
    groovy = client.get_user(234395307759108106)
    #Mute Nathan
    if ctx.author == vivian:
        print("\n")
        print("Message-------------------------")
        print(f"Author: ",{ctx.author})
        print("Message:",ctx.content)
        await ctx.send("shut up nerd")
        return await ctx.delete()
    for i in tiananmen:
        if ctx.content == i:
            return await ctx.delete()
    #1/1000 chance for hannah or reminder
    if ctx.author != client.user and randNumba == 999:
        return await ctx.channel.send(file=discord.File("hannah2.png"))
    if ctx.author != client.user and randNumba == 2:
        return await ctx.channel.send("3. New fucking rule, if you say @ everyone I'm literally gonna revoke your perms")
    elif ctx.author != client.user or ctx.author != groovy:
        print("\n")
        print("Message-------------------------")
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("Author: ",ctx.author)
        print("Message:",ctx.content)
        print("Where:",ctx.guild,"-",ctx.channel)
        return await client.process_commands(ctx)
    
client.run("NzQ3NTI5NzA1OTg0NDkxNTYx.X0QNSg.cFH9NUnCyIt0c6ryv_f4t4WO1-s")

