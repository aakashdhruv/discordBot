import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def join(self, ctx):
    if ctx.author.voice is None:
      await ctx.send("Join a voice channel first!")
    vc = ctx.author.voice.channel
    if ctx.voice_client is None:
      await vc.connect()
      await ctx.send("Joined!")
    else:
      await ctx.voice_client.move_to(vc)
    
  @commands.command()
  async def disconnect(self, ctx):
    await ctx.voice_client.disconnect()
    await ctx.connect("Leaving!")
   
  @commands.command()
  async def play(self, ctx, url):
    ctx.voice_client.stop()
    ffmpegopt = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn' }
    ydlopt = {'format':'bestaudio'}
    

    with youtube_dl.YoutubeDL(ydlopt) as ydl:
      info = ydl.extract_info(url, download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpegopt)
      ctx.voice_client.play(source)
      await ctx.send("Playing song!")

  @commands.command()
  async def pause(self, ctx):
    await ctx.send("Paused ⏸")
    await ctx.voice_client.pause()
    

  @commands.command()
  async def resume(self, ctx):
    await ctx.send("Resumed ⏯")
    await ctx.voice_client.resume()

def setup(client):
  client.add_cog(music(client))

