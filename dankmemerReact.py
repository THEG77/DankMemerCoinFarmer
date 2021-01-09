import discord, time

class MyClient(discord.Client):

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        #if message.author == client.user:
        #    return
        channel = client.get_channel(ENTER CHANNEL ID)
        if message.author.id == 270904126974590976 and message.channel.id == ENTER CHANNEL ID:
            #print("Message from {0.author}: {0.content}".format(message))
            message.content = message.content.replace('﻿','')
            if "god forbid" in message.content:
                print("Interacted with a Dragon !")
            if "god forbid" not in message.content:
                print("Interacting with a Event !")
            if "christmas tree" in message.content:
                time.sleep(1)
                await channel.send("christmas tree")
            elif "north pole" in message.content:
                time.sleep(1)
                await channel.send("north pole")
            elif "christmas card" in message.content:
                time.sleep(1)
                await channel.send("christmas card")
            elif "big bait catches big fish" in message.content:
                time.sleep(1)
                await channel.send("big bait catches big fish")
            elif "What type of meme do you want to post?" in message.content:
                time.sleep(1)
                await channel.send("k")
            elif "yes please" in message.content:
                time.sleep(1)
                await channel.send("yes please")
            elif "oh look a dragon" in message.content:
                time.sleep(1)
                await channel.send("oh look a dragon")
            elif "oh frick a dragon" in message.content:
                time.sleep(1)
                await channel.send("oh frick a dragon")
             elif "pls no eating me" in message.content:
                time.sleep(1)
                await channel.send("pls no eating me")
            elif "woah those are some toothers" in message.content:
                time.sleep(1)
                await channel.send("woah those are some toothers") 
            elif "why didn't I just go fishing" in message.content:
                time.sleep(1)
                await channel.send("why didn't I just go fishing")
            elif "eat lead dragon" in message.content:
                time.sleep(1)
                await channel.send("eat lead dragon")    
            elif "imma kill this dragon" in message.content:
                time.sleep(1)
                await channel.send("imma kill this dragon")
            elif "pls no eating me" in message.content:
                time.sleep(1)
                await channel.send("pls no eating me")                    
            elif "make snow angel" in message.content:
                time.sleep(1)
                await channel.send("make snow angel")                                             
            elif "frick off" in message.content:
                time.sleep(1)
                await channel.send("frick off")
            elif "glub glub glub" in message.content:
                time.sleep(1)
                await channel.send("glub glub glub")
            elif "mistletoe" in message.content:
                time.sleep(1)
                await channel.send("mistletoe")
            elif "krampus is a nerd" in message.content:
                time.sleep(1)
                await channel.send("krampus is a nerd")
            elif "push" in message.content:
                time.sleep(1)
                await channel.send("push")
            elif "dibs" in message.content:
                time.sleep(1)
                await channel.send("dibs")
            elif "happy holidays" in message.content:
                time.sleep(1)
                await channel.send("happy holidays")
            elif "throw snowball" in message.content:
                time.sleep(1)
                await channel.send("throw snowball")
            elif "get the camera ready" in message.content:
                time.sleep(1)
                await channel.send("get the camera ready")
            elif "whoville sucks" in message.content:
                time.sleep(1)
                await channel.send("whoville sucks")
            elif "build snowman" in message.content:
                time(1)
                await channel.send("build snowman")
            elif "hook line sinker" in message.content:
                time.sleep(1)
                await channel.send("hook line sinker")
            elif "disinfect" in message.content:
                print("Found a Karen !")
                for _ in range(1,8):
                    await channel.send("disinfect")
            elif "fuck off karen" in message.content:
                print("Found a Karen !")
                for _ in range(1,8):
                    await channel.send("fuck off karen")        
            elif "lol imagine using skype in 2020" in message.content:
                await channel.send("lol imagine using skype in 2020")
            elif "savage" in message.content:
                await channel.send("savage")
            elif "I forgot dragon repellent again" in message.content:
                await channel.send("I forgot dragon repellent again")    
            elif "why my pls rich no work?" in message.content:
                for _ in range(1,8):
                    await channel.send("why my pls rich no work?")
            elif "f in chat" in message.content:
                await channel.send("f in chat")
            elif "i am so very bored" in message.content:
                await channel.send("i am so very bored")
            elif "wear a mask god damn it" in message.content:
                await channel.send("wear a mask god damn it")
            elif "dragon these nuts on your momma" in message.content:
                await channel.send("dragon these nuts on your momma")
            elif "dragon says rawr" in message.content:
                await channel.send("dragon says rawr")       
            elif "why didn't I just go fishing" in message.content:
                await channel.send("why didn't I just go fishing")    
client = MyClient()
client.run("ENTER TOKEN", bot = False)
