from discord.ext import commands
import discord
import asyncio

class OtherStuff(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Define a new command
    @commands.command(
        name='create-channel',
        brief='Create a channel YOLO',
        description='To create a channel',
        aliases=['c']
    )

    @commands.has_role('Admin')
    async def create_channel(self,ctx, channel_name):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            #print('Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)

    @commands.command(
        name='do',
        brief='Help',
        description='Follow your heart',
        aliases=['sl']
    )
    async def slap(self, ctx, action, person, reason='no reason'):
        await ctx.send('{}, <@{}> {}s you for {}!'.format(str(person),ctx.message.author.id,str(action),reason))


    @commands.command(pass_context=True)
    async def quickpoll(self, ctx, question, *options: str):
        if len(options) <= 1:
            await ctx.send('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot make a poll for more than 10 things!')
            return


        reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        member = ctx.message.author.id
        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description))
        embed.add_field(name="Here you go, ", value=f"<@{ctx.message.author.id}> ")

        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)

        #CHANGE THE TIME
        await asyncio.sleep(5)

        #CAN BE BROKEN EASILY
        react_message = await ctx.fetch_message(react_message.id)

        emojis=[]
        count=[]
        for reaction in react_message.reactions:
            emojis.append(reaction.emoji)
            count.append(int(reaction.count)-1)

        result=dict(zip(emojis,count))

        flag=-1
        max_emoji=""

        for emoji, coun in result.items():
            if coun==0:
                continue
            elif coun == max(count):
                max_emoji=emoji
                flag=0

        if flag==-1:
            max_emoji="Everything"

        embd = discord.Embed(title=question, description=''.join(description))
        embd.add_field(name="Here you go, ", value=f"<@{ctx.message.author.id}> ")
        embd.add_field(name="The results are: ", value='\n'.join(['{}: {}'.format(key,result[key]) for key in result.keys()]))
        embd.add_field(name="Most votes", value='{} got {} votes!'.format(max_emoji,max(count)))
        await react_message.delete()
        await ctx.send(embed=embd)

    @commands.command(
        name='help',
        brief='Help',
        description='Yes, help',
        aliases=['h']
    )
    async def help_ic(self,ctx):
        embed=discord.Embed(title="Ice Cream Bot", description="HELP", color=0xe16f05)
        embed.set_thumbnail(url="https://media.istockphoto.com/vectors/blue-green-ice-cream-fall-vector-id883775310?k=6&m=883775310&s=612x612&w=0&h=mdYLho7shs-VED12ezyadqa_n1HekWHgY-MFWUUD6hE=")

        embed.add_field(name="ICE CREAM STUFF", value="facts, suggest, music, gimme", inline=False)
        embed.add_field(name="facts", value="Sweet sweet fact time", inline=True)
        embed.add_field(name="suggest", value="Suggestions! Type !suggest help for options", inline=True)
        embed.add_field(name="music", value="Specially curated songs", inline=True)
        embed.add_field(name="gimme", value="Gives you the goods. Type !gimme help for options", inline=True)
        embed.add_field(name="educate", value="When facts aren't enough", inline=True)
        embed.add_field(name="weather", value="Can you eat ice-cream now?", inline=True)

        embed.add_field(name="OTHER STUFF", value="create-channel, slap, quickpoll", inline=False)
        embed.add_field(name="create-channel", value="Only for admins! Mention the name as well", inline=True)
        embed.add_field(name="do", value="Follow your heart. !do <action> <person> <reason>", inline=True)
        embed.add_field(name="quickpoll", value="For all the tough decisions", inline=True)
        embed.set_footer(text="The prefix for this bot can be '!' or 'lol'")
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(OtherStuff(bot))
