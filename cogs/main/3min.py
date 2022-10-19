# Imports
from time import perf_counter
import discord
from discord.ext import commands
from discord import app_commands
import json
from discord.ext import tasks
import datetime
configjson = open("config.json")
config = json.load(configjson)

guild = int(config['bot']["serverID"])
mainColour = config['brandingColors']["mainColor"]
reminderChannel = int(config['channels']['main']["reminder"])
reminderRole = int(config['permissions']['main']["reminder"])

configjson.close()


today = datetime.datetime.now(datetime.timezone.utc)
bumpOne = today.replace(hour=23, minute=57, second=0, microsecond=0).time()
bumpTwo = today.replace(hour=5, minute=57, second=0, microsecond=0).time()
bumpThree = today.replace(hour=11, minute=57, second=0, microsecond=0).time()
bumpFour = today.replace(hour=17, minute=57, second=0, microsecond=0).time()

# Cog subclass
class ThreeMinsRemaining(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        self.one.start()
        self.two.start()
        self.three.start()
        self.four.start()

    async def cog_unload(self):
        self.one.cancel()
        self.two.cancel()
        self.three.cancel()
        self.four.cancel()
    @tasks.loop(time=bumpOne, reconnect=True)
    async def one(self):
        channelVar = self.bot.get_channel(reminderChannel) or await self.bot.fetch_channel(reminderChannel)
        if channelVar is None:
            print("[ 🔥 ] Reminder channel not found")
            return
        roleVar = self.bot.get_guild(guild).get_role(reminderRole) or await self.bot.fetch_role(reminderRole)

        embed = discord.Embed(title="⏰ Get ready to bump", description="In **three mins** it will be time to bump! Get ready, the faster you bump the better our server does on Discord.me. Head over to https://discord.me/dashboard to bump!", colour=discord.Colour.from_str(mainColour))
        if roleVar is None:
            await channelVar.send(embed=embed)
        else:
            await channelVar.send(roleVar.mention, embed=embed)
            for member in channelVar.members:
                try:
                    await member.send(embed=embed)
                except:
                    continue


    @tasks.loop(time=bumpTwo, reconnect=True)
    async def two(self):
        channelVar = self.bot.get_channel(reminderChannel) or await self.bot.fetch_channel(reminderChannel)
        if channelVar is None:
            print("[ 🔥 ] Reminder channel not found")
            return
        roleVar = self.bot.get_guild(guild).get_role(reminderRole) or await self.bot.fetch_role(reminderRole)

        embed = discord.Embed(title="⏰ Get ready to bump", description="In **three mins** it will be time to bump! Get ready, the faster you bump the better our server does on Discord.me. Head over to https://discord.me/dashboard to bump!", colour=discord.Colour.from_str(mainColour))
        if roleVar is None:
            await channelVar.send(embed=embed)
        else:
            await channelVar.send(roleVar.mention, embed=embed)
            for member in channelVar.members:
                try:
                    await member.send(embed=embed)
                except:
                    continue

    @tasks.loop(time=bumpThree, reconnect=True)
    async def three(self):
        channelVar = self.bot.get_channel(reminderChannel) or await self.bot.fetch_channel(reminderChannel)
        if channelVar is None:
            print("[ 🔥 ] Reminder channel not found")
            return
        roleVar = self.bot.get_guild(guild).get_role(reminderRole) or await self.bot.fetch_role(reminderRole)

        embed = discord.Embed(title="⏰ Get ready to bump", description="In **three mins** it will be time to bump! Get ready, the faster you bump the better our server does on Discord.me. Head over to https://discord.me/dashboard to bump!", colour=discord.Colour.from_str(mainColour))
        if roleVar is None:
            await channelVar.send(embed=embed)
        else:
            await channelVar.send(roleVar.mention, embed=embed)
            for member in channelVar.members:
                try:
                    await member.send(embed=embed)
                except:
                    continue

    @tasks.loop(time=bumpFour, reconnect=True)
    async def four(self):
        channelVar = self.bot.get_channel(reminderChannel) or await self.bot.fetch_channel(reminderChannel)
        if channelVar is None:
            print("[ 🔥 ] Reminder channel not found")
            return
        roleVar = self.bot.get_guild(guild).get_role(reminderRole) or await self.bot.fetch_role(reminderRole)

        embed = discord.Embed(title="⏰ Get ready to bump", description="In **three mins** it will be time to bump! Get ready, the faster you bump the better our server does on Discord.me. Head over to https://discord.me/dashboard to bump!", colour=discord.Colour.from_str(mainColour))
        if roleVar is None:
            await channelVar.send(embed=embed)
        else:
            await channelVar.send(roleVar.mention, embed=embed)
            for member in channelVar.members:
                try:
                    await member.send(embed=embed)
                except:
                    continue
# Sets up the cog
async def setup(bot):
   await bot.add_cog(ThreeMinsRemaining(bot))