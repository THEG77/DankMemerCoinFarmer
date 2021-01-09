import discord, time, os, random

class MyClient(discord.Client):

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))
        channel = client.get_channel(751276567463854120)
        while True:
            await channel.send("pls hunt")
            time.sleep(5)
            #await channel.send("pls search")
            #time.sleep(5)
            await channel.send("pls fish")
            time.sleep(9)
            await channel.send("pls beg")
            time.sleep(20)
            #await channel.send("pls search")
            time.sleep(5)
            
            await channel.send("pls pm")
            time.sleep(1)
            memeType = random.choice("f","r","i","c","k")
            time.sleep(3)
            await.channel.send(memeType)
            time.sleep(2)
            
            await channel.send("pls beg")
            time.sleep(5)
            await channel.send("pls dep all")
            time.sleep(15)
            
client = MyClient()
token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token, bot = False)
