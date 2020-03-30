import discord
import asyncio
import random
import os
from discord.ext import commands
client = commands.Bot(command_prefix = '-+')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('Young Empire'))
	print('Бот готов.')

@client.command()
@commands.has_any_role('🔥Leader🔥', 'Deputy✅', 'Developer🔨', 'Тех.Администратор🔧')
async def clear(ext, amount=5):
	await ext.channel.purge(limit=amount+1)

@client.command()
async def nick(ext, *, nickname):
	await ext.channel.purge(limit=1)
	member = ext.message.author
	await member.edit(nick=str(nickname))

@client.command()
@commands.has_any_role('🔥Leader🔥', 'Deputy✅', 'Developer🔨', 'Тех.Администратор🔧')
async def mute(ext, member : discord.Member,*, reason):
	if member.id == int(452312332362579998) or member.id == int(433525822956109843) or member.id == int(667712678730530846) or member.id == int(366930064194928650):
		await ext.send("Этому человеку нельзя выдать мут")
	else:
		role = discord.utils.get(ext.guild.roles, name = "Muted")
		await member.add_roles(role)
		await ext.send(f"Выдал мут {member.mention} за {reason}")
	
@client.command()
@commands.has_any_role('🔥Leader🔥', 'Deputy✅', 'Developer🔨', 'Тех.Администратор🔧')
async def unmute(ext, member : discord.Member):
	role = discord.utils.get(ext.guild.roles, name = "Muted")
	await member.remove_roles(role)
	await ext.send(f"Размутил {member.mention}")

def has_id(member):
    def predicate(ext):
        return ext.message.author.id == member
    return commands.check(predicate)

@client.command()
@commands.has_any_role('🔥Leader🔥', 'Deputy✅', 'Developer🔨', 'Тех.Администратор🔧')
async def tempmute(ext, member : discord.Member, time, *, reason):
	if member.id == int(452312332362579998) or member.id == int(433525822956109843) or member.id == int(667712678730530846) or member.id == int(366930064194928650):
		await ext.channel.purge(limit=1)
		await ext.send(ext.message.author.mention + ", этому человеку нельзя выдать мут")
		asyncio.sleep(10)
		await ext.channel.purge(limit=1)
	else:
		role = discord.utils.get(ext.guild.roles, name = "Muted")
		await member.add_roles(role)
		await ext.send(f"Выдал мут {member.mention} на {time} минут за {reason}")
		await asyncio.sleep(float(time) * 60)
		await member.remove_roles(role)
		await ext.send(f"Размутил {member.mention} который был замучен за {reason}")

@client.command()
@commands.has_any_role('🔥Leader🔥', 'Deputy✅', 'Developer🔨', 'Тех.Администратор🔧')
async def unban(ext, *, member):
	await ext.channel.purge(limit=1)
	banned_users = await ext.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ext.guild.unban(user)
			await ext.send(f"Разблокировал {user.mention} который был забанен за '{ban_entry.reason}'")
			return

@client.command()
@commands.has_any_role('🔥Leader🔥', 'Deputy✅', 'Developer🔨', 'Тех.Администратор🔧')
async def kick(ext, member : discord.Member, *, reason=None):
	if member.id == int(452312332362579998) or member.id == int(433525822956109843) or member.id == int(667712678730530846) or member.id == int(366930064194928650):
		await ext.send("Этого человека нельзя кикнуть")
	else:
		await ext.channel.purge(limit=1)
		await ext.send(f"{member.mention} был выгнан за '{reason}'")
		await member.kick(reason=reason)


@client.command()
@commands.has_any_role('🔥Leader🔥', 'Deputy✅', 'Developer🔨', 'Тех.Администратор🔧')
async def ban(ext, member : discord.Member, *, reason=None):
	if member.id == int(452312332362579998) or member.id == int(433525822956109843) or member.id == int(667712678730530846) or member.id == int(366930064194928650):
		await ext.send("Этого человека нельзя забанить")
	else:
		await ext.channel.purge(limit=1)
		await ext.send(f"{member.mention} был заблокирован за '{reason}'")
		await member.ban(reason=reason)

@client.command(aliases=['pings'])
async def ping(ext):
	await ext.send(f"Понг! {round(client.latency * 1000)}ms")

@client.command(aliases = ['8ball'])
async def an8ball(ext, *, question):
	responses = ['Может быть', 'Да', 'Нет']
	await ext.send(f'Вопрос: {question}\nОтвет: {random.choice(responses)}')

@client.event
async def on_member_join(member):
	print(f'{member} присоединился к серверу')
	channel = client.get_channel(667715667528646658)
	await channel.send("Привет " + member.mention)
	embed = discord.Embed(description= "Ты попал на ДС сервер империи Young.Чтобы получить роль, сделай ник по форме: -+nick Имя_Фамилия.")
	await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
	print(f"{member} покинул сервер")
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
