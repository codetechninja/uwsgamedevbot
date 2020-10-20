import discord
from discord.ext import commands


class GameDevDictionary(commands.Cog):
    """The `GameDevDictionary` class"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def tutorials(self, ctx):
        """Command Description"""
        return await self.bot.send_message(ctx.message.channel, "See how to use this command by running `{}help tutorials`".format(ctx.prefix))

    @commands.command(pass_context=True, name='DictionaryTest')
    async def test(self, ctx):
        await ctx.send('Dictionary Test Working')

    @commands.command(pass_context=True, name='Info')
    async def DInfo(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title="Game Development Dictionary",
                              description="this module allows you to put in terms related to game dev and get more information and resources for example !Unity would pull up links related to Unity. ",
                              color=0xffffff)
        embed.add_field(name="Current terms in the dictionary", value="More to come", inline=False)
        embed.add_field(name="1", value="!General", inline=False)
        embed.add_field(name="2", value="!Unity", inline=False)
        embed.add_field(name="3", value="!Unreal", inline=False)
        embed.add_field(name="4", value="!Godot", inline=False)
        embed.add_field(name="5", value="!Art", inline=False)
        embed.add_field(name="6", value="!Programming", inline=False)
        embed.add_field(name="7", value="!Audio", inline=False)
        embed.add_field(name="8", value="!Shaders", inline=True)
        await ctx.send(channel, embed=embed)

    @commands.command(pass_context=True, name='General')
    async def GeneralInfo(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title="Global", description="General Games Development Resources ", color=0x282d86)
        embed.add_field(name="Game Dev Data base", value="https://gamedevelop.io/resources", inline=False)
        embed.add_field(name="GDC Vault", value="https://www.gdcvault.com/free", inline=False)
        embed.add_field(name="reddit Games development", value="https://www.reddit.com/r/gamedev/", inline=False)
        embed.add_field(name="learn anything general resource", value="https://learn-anything.xyz", inline=False)
        embed.add_field(name="more resources", value="https://www.gamedev.net/", inline=False)
        embed.add_field(name="industry news", value="https://www.gamesindustry.biz/", inline=False)
        embed.add_field(name="news software/tools", value="https://gamefromscratch.com/", inline=False)
        await ctx.send(channel, embed=embed)

    @commands.command(pass_context=True, name='Unity')
    async def Unity(self,ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title="Unity", description="Unity resources ", color=0x000000)
        embed.add_field(name="Unity learning website", value="https://learn.unity.com/", inline=False)
        embed.add_field(name="unity documentation", value="https://docs.unity3d.com/Manual/index.html", inline=False)
        embed.add_field(name="unity forums", value="https://answers.unity.com/index.html", inline=False)
        embed.add_field(name="unity reddit", value="https://www.reddit.com/r/Unity3D/", inline=False)
        await ctx.send(channel, embed=embed)

    @commands.command(pass_context=True, name='Unreal')
    async def Unreal(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title="Unreal Engine", description="Unreal Engine resources", color=0xdea309)
        embed.add_field(name="Unreal learning site",
                        value="https://www.unrealengine.com/en-US/onlinelearning-courses?sessionInvalidated=true",
                        inline=False)
        embed.add_field(name="Unreal Engine Docuumentation", value="https://docs.unrealengine.com/en-US/index.html",
                        inline=False)
        embed.add_field(name="Unreal engine Reddit", value="https://www.reddit.com/r/unrealengine/", inline=False)
        embed.add_field(name="Community wiki", value="https://www.ue4community.wiki/", inline=False)
        embed.add_field(name="different tutorial", value="https://www.raywenderlich.com/unreal-engine", inline=False)
        await ctx.send(channel, embed=embed)

    @commands.command(pass_context=True, name='Godot')
    async def Godot(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title="Godot", description="Dodot Resources", color=0x3590be)
        embed.add_field(name="godot website", value="https://godotengine.org/", inline=False)
        embed.add_field(name="Godot documentation", value="https://docs.godotengine.org/en/stable/index.html",
                        inline=False)
        embed.add_field(name="Reddit Godot", value="https://www.reddit.com/r/godot/", inline=False)
        await ctx.send(channel, embed = embed)

    @commands.command(pass_context=True, name='Art')
    async def Art(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title="Art", description="General game Art", color=0xff2828)
        embed.add_field(name="massive art resource page",
                        value="https://www.notion.so/The-Empire-Command-3a3bf979f8df4ca2a49315bc0dc31f9f", inline=False)
        embed.add_field(name="Artstation learning", value="https://www.artstation.com/learning", inline=False)
        embed.add_field(name="Art news site", value="https://80.lv/", inline=False)
        embed.add_field(name="game art forum", value="https://polycount.com/", inline=False)
        embed.add_field(name="Blender resources mix", value="https://www.blendernation.com/", inline=False)
        embed.add_field(name="flipped normals", value="https://flippednormals.com/", inline=False)
        embed.add_field(name="collab drawing program", value="https://magmastudio.io/", inline=False)
        await ctx.send(channel, embed = embed)

    @commands.command(pass_context=True, name='Programming')
    async def Programming(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title="Programming", description="General programming resources", color=0x9fd6d7)
        embed.add_field(name="Programming patterns", value="shorturl.at/fgrMU", inline=False)
        embed.add_field(name="Infallible Code ", value="shorturl.at/cgGLQ", inline=False)
        embed.add_field(name="General Resources",
                        value="shorturl.at/M4679", inline=False)
        embed.add_field(name="Lean C# by building a rpg",
                        value="shorturl.at/qrwR2", inline=False)
        embed.add_field(name="c# book",
                        value="shorturl.at/oqwM7",
                        inline=False)
        embed.add_field(name="Beginning C++ Through Game Programming by Michael Dawson",
                        value="shorturl.at/xABNU", inline=False)
        await ctx.send(channel, embed = embed)

    @commands.command(pass_context=True, name='Audio')
    async def Audio(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title="Audio", description="Game Audio Resources", color=0xf03cd6)
        embed.add_field(name="Reddit Game Audio wiki", value="https://www.reddit.com/r/GameAudio/wiki/", inline=False)
        embed.add_field(name="gamasutra design game audio",
                        value="https://www.gamasutra.com/blogs/PavelShylenok/20190506/342095/Designing_Sounds_for_a_Game.php",
                        inline=False)
        embed.add_field(name="Game design learn audio design",
                        value="https://www.gamedesigning.org/learn/video-game-sound/", inline=False)
        await ctx.send(channel, embed = embed)

    @commands.command(pass_context=True, name='Shaders')
    async def Shaders(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title="Shader", description="Shaders resources", color=0x69ed7a)
        embed.add_field(name="book of shaders", value="http://thebookofshaders.com", inline=False)
        embed.add_field(name="Shader resource archive", value="http://halisavakis.com/archive/", inline=False)
        embed.add_field(name="shaderlab", value="http://www.shaderslab.com", inline=False)
        await ctx.send(channel, embed = embed)


def setup(bot):
    """Method that loads this module into the client"""
    bot.add_cog(GameDevDictionary(bot))
    print("GameDevDictionary module loaded.")
