from discord.ext import tasks,commands
import os
import discord
import random
import asyncio
from dotenv import load_dotenv
import sys, traceback
from discord.utils import get
from requests import get as rget


load_dotenv()
API_KEY = os.getenv('API_KEY')

class IceCreamStuff(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #gets random facts
    @commands.command(
        name='facts',
        brief='Sweet sweet ice-cream facts!',
        description='For sweet sweet ice-cream facts!',
        aliases=['f']
    )

    async def ice_cream_facts(self,ctx):
            ice_cream_facts = [
                'The most popular flavor of ice cream is vanilla. After it come chocolates, strawberry, cookies n’ cream, and others.',
                'Biggest ice cream sundae was created in Edmonton, Alberta, Canada in 1988. It weighted 24 tons.',
                'One of the most unusual ice cream flavors is hot dog flavored ice-cream that was created in Arizona, US.',
                'Hawaii is a home to an “ice cream bean”, fruit that tastes like vanilla ice cream.',
                'Market analysts confirmed that ice cream sales increase many times during times of recession or wars.',
                'One cone of ice cream can be finished off in 50 licks.',
                'Why is your definition of self care ice cream facts? Go regret your life decisions',
                'Ice cream can be made in many types – ordinary ice cream, frozen custard, frozen yogurt, reduced-fat ice cream, sherbet, gelato, and others.'
            ]

            response = random.choice(ice_cream_facts)
            await ctx.send(f"<@{ctx.message.author.id}> "+response)

    #suggest stuff based on input
    @commands.command(
        name='suggest',
        brief="Suggestions! Type !suggest help for options",
        description='Ice Cream Suggestions!',
        aliases=['s']
    )
    async def ice_cream_sug(self,ctx,sug):

            ice_cream_sug = {"help":"Help:","Sweet":"Chocolate","Plain":"Vanilla","Brown":"Chocolate","White":"Vanilla"}
            if sug=="help":
                embed=discord.Embed(title="Here are your options!",color=0xe16f05)
                embed.set_author(name="Ice Cream Bot")
                embed.set_thumbnail(url="https://4.imimg.com/data4/FX/KY/MY-1579893/flavours-for-ice-cream-500x500.jpg")
                embed.add_field(name="Flavour", value="Sweet, Plain      ", inline=True)
                embed.add_field(name="Colour", value="Brown, White     ", inline=True)
                embed.set_footer(text="Try !suggest option-name")
                await ctx.send(embed=embed)
            else:
                response = ice_cream_sug[sug]
                await ctx.send(f"<@{ctx.message.author.id}> "+response)

    #fetches weather data
    @commands.command(
        name='weather',
        brief="Weather stuff",
        description='Is a good time to eat ice-cream?',
        aliases=['w']
    )
    async def ice_cream_weather(self,ctx,city,forecast=False):

            key = API_KEY

            if forecast:
                return rget(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&APPID={key}").json()
            data  = rget(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={key}").json()

            temp=data['main']['temp']

            if temp>=27:
                await ctx.send(f"<@{ctx.message.author.id}>, "+"the temperature is {} degree Celsius in {}! We all know how to beat the summer blues :)".format(temp,city.capitalize()))
            else:
                await ctx.send(f"<@{ctx.message.author.id}>, "+"the temperature is {} degree Celsius in {}! Perfect time to eat ice-cream and be one with the nature :)".format(temp,city.capitalize()))

    #spams, has bugs
    @commands.command(
        name='educate',
        brief="More facts",
        description="When facts aren't enough",
        aliases=['e']
    )
    async def ice_cream_ed(self,ctx,com=""):

            #original feature ideas 404
            #try webscraping instead of this mess :")
            sentences = [
                "Ice cream (derived from earlier iced cream or cream ice) is a sweetened frozen food typically eaten as a snack or dessert",
                "It may be made from dairy milk or cream and is flavoured with a sweetener, either sugar or an alternative, and any spice, such as cocoa or vanilla.",
                "Colourings are usually added, in addition to stabilizers.",
                "The mixture is stirred to incorporate air spaces and cooled below the freezing point of water to prevent detectable ice crystals from forming.",
                "The result is a smooth, semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F).",
                "It becomes more malleable as its temperature increases",
                'The meaning of the name "ice cream" varies from one country to another. Terms such as "frozen custard," "frozen yogurt," "sorbet," "gelato," and others are used to distinguish different varieties and styles.',
                'In some countries, such as the United States, "ice cream" applies only to a specific variety, and most governments regulate the commercial use of the various terms according to the relative quantities of the main ingredients, notably the amount of cream.',
                'Products that do not meet the criteria to be called ice cream are sometimes labelled "frozen dairy dessert" instead.',
                'In other countries, such as Italy and Argentina, one word is used for all variants.',
                "Analogues made from dairy alternatives, such as goat's or sheep's milk, or milk substitutes (e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are lactose intolerant, allergic to dairy protein, or vegan."

            ]
            if com=="stop":
                await ctx.send(f"<@{ctx.message.author.id}>, "+"coward.")
                #shuts down the cursed bot
                #why is the documentation so convulated
                quit()
            else:
                await ctx.send(f"<@{ctx.message.author.id}>, "+"your thirst for knowledge is commendable!")
                for sentence in sentences:
                    await asyncio.sleep(2)
                    await ctx.send(sentence)

    #reacts to messages
    @commands.command(
       name='gimme',
       brief="Gives",
       description='Does what it should',
       aliases=['r'])

    async def tick(self,ctx,message):

        choices = {
          "normal": '🍨',
          "shaved": '🍧',
          "soft":'🍦',
        }

        edgy=['🇪','🇩','🇬','🇾']

        if message=="help":
            embed=discord.Embed(title="Here are your options!",color=0xe16f05)
            embed.set_author(name="Ice Cream Bot")
            embed.set_thumbnail(url="https://4.imimg.com/data4/FX/KY/MY-1579893/flavours-for-ice-cream-500x500.jpg")
            embed.add_field(name="Option", value="normal, shaved, soft, random")
            embed.set_footer(text="Try !gimme option-name")
            await ctx.send(embed=embed)
        elif message in choices:
            await ctx.message.add_reaction(choices[message])
        elif message=="random":
            response = random.choice(list(choices.keys()))
            await ctx.message.add_reaction(choices[response])
        else:
            for emoji in edgy:
                await ctx.message.add_reaction(emoji)


    #suggests music, very noobish
    @commands.command(
        name='music',
        brief="To blow your minds",
        description='Ice Cream Suggestions UwU!',
        aliases=['m']
    )
    async def ice_music(self,ctx):
        music_sug=['1','2','3']
        resp = random.choice(music_sug)
        if resp=='1':
            embed = discord.Embed(title='Ice-Cream Cake - Red Velvet',
                           url='https://youtu.be/glXgSSOKlls',
                           description='Gimme that, gimme that ice cream',
                           color=0xfbff00)
            embed.add_field(name="now ᴘʟᴀʏɪɴɢ:",value="───────────⚪────── ◄◄⠀▐▐⠀►► 𝟸:𝟷𝟾 / 𝟹:2𝟼⠀───○ 🔊", inline=True)
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/e/e3/Ice_Cream_Cake_%28EP%29.jpg")
            embed.add_field(name="Here you go,", value=f"<@{ctx.message.author.id}> ")
            await ctx.send(embed=embed)
        if resp=='2':
            embed = discord.Embed(title='Ice-Cream Song - Twice',
                           url='https://youtu.be/dQw4w9WgXcQ',
                           description="Can't be described",
                           color=0xfbff00)
            embed.add_field(name="now ᴘʟᴀʏɪɴɢ:",value="───────────⚪────── ◄◄⠀▐▐⠀►► 𝟸:2𝟾 / 𝟹:12⠀───○ 🔊", inline=True)
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/e/e3/Ice_Cream_Cake_%28EP%29.jpg")
            embed.add_field(name="Here you go,", value=f"<@{ctx.message.author.id}> ")
            await ctx.send(embed=embed)
        if resp=='3':
            embed = discord.Embed(title='Ice-Cream - HyunA',
                           url='https://www.youtube.com/watch?v=QlWZluzBNxM',
                           description='None of us deserve this.',
                           color=0xfbff00)
            embed.add_field(name="now ᴘʟᴀʏɪɴɢ:",value="───────────⚪────── ◄◄⠀▐▐⠀►► 𝟸:55 / 4:00⠀───○ 🔊", inline=True)
            embed.set_thumbnail(url="https://i.ytimg.com/vi/7p8NzGoahf0/maxresdefault.jpg")
            embed.add_field(name="Here you go,", value=f"<@{ctx.message.author.id}> ")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(IceCreamStuff(bot))
