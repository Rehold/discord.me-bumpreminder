# Imports
import discord
from discord.ext import commands
from discord import app_commands, Colour
from typing import List
import json

# Cog subclass
class SetupCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # Allows us to use the bot outside of the __init__ function
        self.bot.tree.add_command(setupcommand) # Register the slash command in our bot


configjson = open("config.json")
# config should be file name, () gotta be var above
config = json.load(configjson)
serverID = int(config['bot']["serverID"])
requiredRole = int(config['permissions']['admin']['setup'])
mainColor = config['brandingColors']["mainColor"]
errorColor = config['brandingColors']["errorColor"]
successColor = config['brandingColors']["successColor"]
configjson.close()


@app_commands.command(name="setup", description="Setup the bot.")
@app_commands.checks.has_role(requiredRole)
@app_commands.guilds(serverID)
@app_commands.describe(channel="The channel to remind you in.", role="The role to ping when you get reminded.")
async def setupcommand(interaction: discord.Interaction, channel: discord.TextChannel, role: discord.Role = None):
    if role is None:
        role = ""
    else:
        config["permissions"]["main"]["reminder"] = str(role.id)
    config["channels"]["main"]["reminder"] = str(channel.id)

    with open("config.json", "w") as jsonFile:
        json.dump(config, jsonFile, indent=4)

    await interaction.response.send_message(f"Setup complete!\n\nReminder channel: {channel.mention}\nReminder role: {role.mention if role != '' else 'None'}")


@setupcommand.error
async def sync_error(
    interaction: discord.Interaction, error: app_commands.AppCommandError
):
    if isinstance(error, app_commands.MissingRole):
        embed = discord.Embed(
            title="⛔ No permission",
            description="You do not have the required permission to run this command!",
            colour=Colour.from_str(errorColor),
        )
        embed.add_field(name="Role required:", value=f"<@&{requiredRole}>")
        await interaction.response.send_message(embed=embed)
        return
    raise error

# Sets up the cog
async def setup(bot):
    await bot.add_cog(SetupCmd(bot))