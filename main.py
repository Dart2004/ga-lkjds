import discord
client=discord.Client()
import dic
import time
client.prefix=">"
know=dict(dic.dicti)
g=False
@client.event
async def on_message(message):
	global g,know,dic,question,answer
	if message.author==client.user:
		return
	message.content=message.content.lower()
	if client.prefix in message.content:
		try:
			if message.content=="runtime":
				await message.channel.send(time.process_time())
				return
			await message.channel.send(know[message.content.replace(client.prefix,"")])
		except:
			pass
	elif g==False:
		print(message.content)
		g=True
		question=message.content
	elif g==True:
		print(message.content)
		g=False
		answer=message.content
		if question not in know.keys():
			print(str(know))
			know[question]=answer
			d=open("dic.py","w")
			d.write("dicti="+str(know))
client.run("NjU5NzYyMTc4OTM2Nzk5MjU4.XkgIIg.SFbMzjQmmZtwQtjRKW2b7ZJsSSI")
