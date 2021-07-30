import datetime
import socket
import discord
import requests
import os
import sendgrid
from discord.ext import commands
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

prefix = '>'
bot = commands.Bot(help_command=None, command_prefix=prefix)

# Add your own Discord IDS
Gangsters = [796455044891410452, 836177255948222504, 352292720301047808]

@bot.event
async def on_ready():
    activity = discord.Game(name=f"{prefix}help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("[skokie-mailer online]", bot.user)

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Help / Usage',
        color = 0x1FFF00
    )

    embed.timestamp = datetime.datetime.utcnow()

    embed.add_field(name="Prefix Command:", value=prefix)
    embed.add_field(name="Commands:", value=(f"```{prefix}mail fromSpoofedEmail toEmail subject message```"), inline=False)
    embed.set_footer(text='skokie-mailer/uwu-edition')

    await ctx.send(embed=embed)

@bot.command()
async def mail(ctx, fromSpoofedEmail : str = None, toEmail : str = None, subject : str = None, message : str = None):
    if ctx.author.id not in Gangsters:

        embed = discord.Embed(
            title = 'Insufficient Permissions',
            color = 0x1FFF00
        )

        await ctx.send(embed=embed)

    elif ctx.author.id in Gangsters:

        message2 = Mail(
        from_email=fromSpoofedEmail,
        to_emails=toEmail,
        subject=subject,
        html_content=message)
        
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message2)
        print(response.status_code, response.body, response.headers)

        embedSuccess = discord.Embed(
            title = ':white_check_mark: Successfully sent Email!',
            color = 0x1FFF00
        )

        embedSuccess.timestamp = datetime.datetime.utcnow()

        embedSuccess.add_field(name="From Email:", value=f"```{fromSpoofedEmail}```", inline=False)
        embedSuccess.add_field(name="To Email:", value=f"```{toEmail}```", inline=False)
        embedSuccess.add_field(name="Subject:", value=f"```{subject}```", inline=False)

        if len(message) >= 1000:
            message = "Message is greater than 1000 (Unable to show)"

        embedSuccess.add_field(name="Message:", value=f"```{message}```", inline=False)

        embedSuccess.set_footer(text='skokie-mailer/uwu-edition')
        

        await ctx.send(embed=embedSuccess)

bot.run("bot_token")
