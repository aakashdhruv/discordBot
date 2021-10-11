import discord
from discord.ext import commands

#import cogs
import music
import fun
import songSuggestor
#import songRater

#add cogs to initialize
cogs = [music, fun, songSuggestor]

bot = commands.Bot(
    command_prefix="s!",  
  # For now, please use your name as a prefix
    case_sensitive=True
)


for i in range(len(cogs)):
  cogs[i].setup(bot)

bot.author_id = 357337245318905856  # Your Discord ID

@bot.event 
async def on_ready():  # When the bot is ready:
  await bot.change_presence(status = discord.Status.online, 
  activity = discord.Activity(type=discord.ActivityType.listening, name="s!"))
  print("Bot is running.")


#runs bot
bot.run("ODkyODU0MDc4MDE3Nzg5OTgz.YVS9KA.0prwBOEyJYK_aehGohAOV33gVqs") 
