"""
# Code for DISCORD bot that uses ROBLOX API and DISCORD API
# DISCORD API to deliver messages to a webhook or other output
# ROBLOX API to track updates and send a notification via DISCORD API
# Check if a game was updated every 5 minutes(variable)
# When a game updates, ping the role Gunters.
"""

import discord
import os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
from time import time

load_dotenv()

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()  # Registers all slash commands globally
    print(f"Logged in as {bot.user}!")


@bot.tree.command(name="hello", description="Say hello!")
@app_commands.describe(user="The user you want to ping")
async def hello(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f"Hello {user.mention}")


@bot.tree.command(name="watch", description="Says the time")
async def GETTime(interaction: discord.Interaction):
    await interaction.response.send_message(f"The time is {time()}")


bot.run(TOKEN)
