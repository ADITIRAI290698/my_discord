import discord
client = discord.Client()

#list of words to interact with the bot

lst = ['hello','Hello','Hi','hi','hey','Hey','HEY','HELLO','HI']

#Function which gets executed reach time bot is called
@client.event
async def on_ready():
  print("Hello everyone this is the bot speaking")
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content in lst:
        await message.channel.send(f'Hi user {message.author.roles} belonging to server name : {message.guild.name} in channel {message.channel.name}')

#Calling of bot(function)
client.run('MTAwNTUwOTA4MDkzODQ1OTE2Ng.GR3R-p.70DzfJ2H7cqM4CS_Wv3JYQ_kUJ6bRjw2rtY2F4')