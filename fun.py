from discord.ext import commands


class fun(commands.Cog):
  #nfl
  @commands.command()
  async def dal(self, ctx): 
      await ctx.send("dallas cowboys suck")

  @commands.command()
  async def phi(self, ctx):
      await ctx.send("philadelphia eagles rule\nhttps://www.youtube.com/watch?v=4ujS__0MQMo")

  #don't
  @commands.command()
  async def morty(self, ctx):
      await ctx.send('<https://www.youtube.com/watch?v=iik25wqIuFo>')

  #coochie man
  @commands.command()
  async def coochie(self, ctx):
      await ctx.send("https://tenor.com/view/coochie-man-c00chieman-im-different-gif-18837712")

def setup(client):
  client.add_cog(fun(client))
