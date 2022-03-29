import discord 
import os
from dotenv import load_dotenv


bot=discord.Client()
load_dotenv()
bot_key=os.environ.get('bot_api_key')


#################################################################################################################################################
######################################################## BOT EVENTS #############################################################################
#################################################################################################################################################

@bot.event
async def on_ready():
	print('Logged in as {}'.format(bot.user))


@bot.event
async def on_message(message):
	if message.author==bot.user:
		pass

	# Greeting message
	if message.content.startswith('!hello') or message.content.startswith('!hi') or message.content.startswith('!hey'):
		embed=discord.Embed(description=greeting_message.format(message.author))
		embed.color=embed_color
		await message.channel.send(embed=embed)

	# sample
	if message.content.startswith('!commandname query'):
		query=message.content.split(' ')[-1]
		print('Query is : ',query)

		# perform function on query as input

		# result is output from function
		result=query

		embed=discord.Embed(title='name of function',description=' content output -> {}'.format(result))
		embed.color=embed_color
		await message.channel.send(embed=embed)

	# sample help
	if message.content.startswith('!commandname help'):
		embed=discord.Embed(title='Helper for query',description=' about ')
		embed.color=embed_color
		await message.channel.send(embed=embed)




#################################################################################################################################################
######################################################## FUNCTIONS  #############################################################################
#################################################################################################################################################




#################################################################################################################################################
######################################################## VARIABLES  #############################################################################
#################################################################################################################################################

embed_color=0x0a528c
greeting_message='''Hello there {} :wave: Glad to meet you ! Use `!help` to see the list of available commands.'''



bot.run(bot_key)
