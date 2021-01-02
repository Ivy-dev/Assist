class MODERATION():
    __version__ = 1.1

import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
from pyfiglet import Figlet
from termcolor import colored 
import requests


import json
import os

if os.path.exists(os.getcwd() + "/config.json"):

    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "."}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix = prefix,  case_insensitive=True, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():          
   await bot.change_presence(activity=discord.Game(name="Prefix is - | #AssistOT")) # This is the bots status, Playing...
   print(f"{bot.user.name} is now online | Prefix: {prefix} | Version: {MODERATION.__version__}  ")


@bot.group(invoke_without_command=True)
async def help(ctx):
    embed=discord.Embed(title="Help | Team Assist", description=f"Command usage: `{prefix}help <category/cmd>`", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.add_field(name=":file_folder: General ", value=f"`{prefix}help general` ", inline=True)
    embed.add_field(name=":tools: Moderation ", value=f"`{prefix}help moderation` ", inline=True)
    embed.add_field(name=":performing_arts: Fun ", value=f"`{prefix}help fun` ", inline=True)
    embed.add_field(name=":warning: AntiNuke ", value=f"`{prefix}help anti` ", inline=True)
    embed.add_field(name=":busts_in_silhouette: Team ", value=f"`{prefix}help team` ", inline=True)
    embed.add_field(name=":wave: Welcome ", value=f"`{prefix}help welcome` ", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(aliases=["mod"])
async def moderation(ctx):
    embed=discord.Embed(title="Moderation | Team Assist", description=f"Command usage: `{prefix}help <cmd>`", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.add_field(name="`Ban`", value=f"`{prefix}Help ban` ", inline=True)
    embed.add_field(name="`Kick`", value=f"`{prefix}Help kick` ", inline=True)
    embed.add_field(name="`Mute`", value=f"`{prefix}Help mute` ", inline=True)
    embed.add_field(name="`Purge`", value=f"`{prefix}Help purge` ", inline=True)
    embed.add_field(name="`Unban`", value=f"`{prefix}Help unban` ", inline=True)
    embed.add_field(name="`Unmute`", value=f"`{prefix}Help unmute` ", inline=True)
    embed.add_field(name="`Nuke`", value=f"`{prefix}Help nuke` ", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(aliases=["gen"])
async def general(ctx):
    embed=discord.Embed(title="General | Team Assist", description=f"Command usage: `{prefix}help <cmd>`", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.add_field(name="`Whois`", value=f"`{prefix}Help whois` ", inline=True)
    embed.add_field(name="`Avatar`", value=f"`{prefix}Help avatar` ", inline=True)
    embed.add_field(name="`Ping`", value=f"`{prefix}Help ping` ", inline=True)
    embed.add_field(name="`Serverinfo`", value=f"`{prefix}Help serverInfo` ", inline=True)
    embed.add_field(name="`DM`", value=f"`{prefix}Help DM` ", inline=True)
    embed.add_field(name="`ADM`", value=f"`{prefix}Help ADM` ", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command()
async def fun(ctx):
    embed=discord.Embed(title="Fun | Team Assist", description=f"Command usage: `{prefix}help <cmd>`", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.add_field(name="`8ball`", value=f"`{prefix}Help 8ball` ", inline=True)
    embed.add_field(name="`Relevance`", value=f"`{prefix}Help relevance` ", inline=True)
    embed.add_field(name="`Hack`", value=f"`{prefix}Help hack` ", inline=True)
    embed.add_field(name="`GreenText`", value=f"`{prefix}Help greenText` ", inline=True)
    embed.add_field(name="`Dog`", value=f"`{prefix}Help dog` ", inline=True)
    embed.add_field(name="`Gay`", value=f"`{prefix}Help gay` ", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(aliases=["assist"])
async def Team(ctx):
    embed=discord.Embed(title="Team | Team Assist", description=f"Command usage: `{prefix}help <cmd>`", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.add_field(name="`Socials`", value=f"`{prefix}Help socials` ", inline=True)
    embed.add_field(name="`Roster`", value=f"`{prefix}Help roster` ", inline=True)
    embed.add_field(name="`Rules`", value=f"`{prefix}Help rules` ", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command()
async def Anti(ctx):
    await ctx.send("*coming soon...*")

@help.command(name="8ball")
async def eightball_func(ctx):
    embed=discord.Embed(title="8ball | Team Assist", description=f"**Usage:** {prefix}8ball [question]\n**Description:** Answers your question\n**Permissions Needed:** None", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(name="relevance")
async def relevance_func(ctx):
    embed=discord.Embed(title="Relevance | Team Assist", description=f"**Usage:** {prefix}Relevance [user]\n**Description:** Shows the users relevance\n**Permissions Needed:** None", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(name="green")
async def green_func(ctx):
    embed=discord.Embed(title="Green Text | Team Assist", description=f"**Usage:** {prefix}greentext [message]\n**Description:** Makes the message green\n**Permissions Needed:** None", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(aliases=["howgay"])
async def gay(ctx):
    embed=discord.Embed(title="Gay | Team Assist", description=f"**Usage:** {prefix}gay [user]\n**Description:** Shows how gay the mentioned user is\n**Permissions Needed:** None", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)














@help.command(name="dog")
async def dog_func(ctx):
    embed=discord.Embed(title="Dog | Team Assist", description=f"**Usage:** {prefix}dog\n**Description:** Returns a cute dog\n**Permissions Needed:** None", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(name="ban")
async def ban_func(ctx):
    embed=discord.Embed(title="Ban | Team Assist", description=f"**Usage:** {prefix}ban [user] (reason)\n**Description:** Bans the mentioned user from the server\n**Permissions Needed:** ban_members", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(name="kick")
async def kick_func(ctx):
    embed=discord.Embed(title="Kick | Team Assist", description=f"**Usage:** {prefix}kick [user] (reason)\n**Description:** Kicks the mentioned user from the server\n**Permissions Needed:** kick_members", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(name="mute")
async def mute_func(ctx):
    embed=discord.Embed(title="Mute | Team Assist", description=f"**Usage:** {prefix}mute [user] (reason)\n**Description:** Mutes the mentioned user\n**Permissions Needed:** manage_roles", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(name="purge")
async def purge_func(ctx):
    embed=discord.Embed(title="Purge | Team Assist", description=f"**Usage:** {prefix}purge [amount]\n**Description:** Purges the amount of messages specified\n**Permissions Needed:** manage_messages", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@help.command(name="unmute")
async def unmute_func(ctx):
    embed=discord.Embed(title="Unmute | Team Assist", description=f"**Usage:** {prefix}unmute [user]\n**Description:** Unmutes the mentioned user\n**Permissions Needed:** manage_roles", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(name="nuke")
async def nuke_func(ctx):
    embed=discord.Embed(title="Nuke | Team Assist", description=f"**Usage:** {prefix}nuke [channel]\n**Description:** Purges all messsages in the channel\n**Permissions Needed:** manage_server", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@help.command(name="Unban")
async def Unban_func(ctx):
    embed=discord.Embed(title="Unban | Team Assist", description=f"**Usage:** {prefix}unban [user]\n**Description:** Unbans the mentioned user\n**Permissions Needed:** ban_members", color=0x7ecc7, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)



@bot.command(aliases=["green"])
async def greentext(ctx, *, message):
    await ctx.send(f'```bash\n "{message}" ```')

    












































@bot.command(aliases=['woofer', 'puppy'])
async def dog(ctx):
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    embed = discord.Embed(title="Awww a cute dog 🐶 ", color=0x7ecc7)
    embed.set_image(url=str(r['message']))
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    try:
        await ctx.send(embed=embed)
    except:
        await ctx.send(str(r['message']))



@bot.command(aliases=["rename"])
@commands.has_permissions(administrator=True)
async def guildname(ctx, *, arg):
    embed = discord.Embed(description=f"***{ctx.guild.name} has been successfully been renamed to {arg}***", color=0x7ecc7)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.guild.edit(name=arg)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    embedhi=discord.Embed(description=f"***{member.name} has been banned***", color=0x7ecc7)
    embedhi.set_footer(text=f"Command invoked by: {ctx.author}", icon_url=ctx.author.avatar_url)
    embed=discord.Embed(description=f"**You have been banned from Team Assist | Reasoning: {reason}**",color=0x7ecc7)
    await member.send(embed=embed)
    await member.ban(reason=reason)
    await ctx.send(embed=embedhi)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    embedhi=discord.Embed(description=f"***{member.name} has been kicked***", color=0x7ecc7)
    embed=discord.Embed(description=f"**You have been kicked from Team Assist | Reasoning: {reason}**",color=0x7ecc7)
    await member.send(embed=embed)
    await member.ban(reason=reason)
    await ctx.send(embed=embedhi)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def Mute(ctx, member : discord.Member, *, reason=None):
    embed = discord.Embed(description = f"***{member.name} has been muted***", color=0x7ecc7)
    embedreason = discord.Embed(description=f"**You have been muted in Team Assist | Reasoning: {reason}**",color=0x7ecc7)
    muted_role = ctx.guild.get_role(789877277390798848)
    await member.add_roles(muted_role, reason=reason)
    await member.send(embed=embedreason)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def Unmute(ctx, member : discord.Member, *, reason=None):
    embed = discord.Embed(description = f"***{member.name} has been unmuted***", color=0x7ecc7)
    embedmsg = discord.Embed(description=f"**You have been unmuted in Team Assist**", color=0x7ecc7)
    muted_role = ctx.guild.get_role(789877277390798848)
    await member.remove_roles(muted_role, reason=reason)
    await member.send(embed=embedmsg)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_guild=True)
@commands.cooldown(1, 50, commands.BucketType.guild)
async def nuke(ctx):
    channel_info = [ctx.channel.category,
                    ctx.channel.position]
    chann = await ctx.channel.clone()
    await ctx.channel.delete()
    embed = discord.Embed(
        title=f"Successfully Nuked `{ctx.channel.name}`.", color=0x7ecc7, timestamp=ctx.message.created_at)
    new_channel = channel_info[0].text_channels[-1]
    await new_channel.edit(position=channel_info[1])
    embed.set_footer(
        text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(
        url="https://media.discordapp.net/attachments/794226677907587094/794689589528756254/assistrippler.gif")
    await chann.send(embed=embed)




















bot.run(token)