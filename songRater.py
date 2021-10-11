import discord
from discord.ext import commands

cartiList = [
  "Bloody\nhttps://www.youtube.com/watch?v=1qLgu0bE-Fc",
  "Where the Hell we Going\nhttps://www.youtube.com/watch?v=WCrPMRusO2c", 
  "New Tank\nhttps://www.youtube.com/watch?v=nQC6MyBHceE" 
  "Sky\nhttps://www.youtube.com/watch?v=GYE9H4SMq5E", 
  "RIP\nhttps://www.youtube.com/watch?v=Mldiut-hsmc", 
  "9 AM in Calabasas\nhttps://www.youtube.com/watch?v=0poJEsMqaak",
  "Whole Lotta Sunrise\nhttps://www.youtube.com/watch?v=ke8X2JjYWaQ",
  "One Day\nhttps://www.youtube.com/watch?v=NW69qa2_K3Y",
  "Cancun on SEGA\nhttps://www.youtube.com/watch?v=mBaYKWGhXmM",
  "Can't Relate\nhttps://www.youtube.com/watch?v=RfKAujoZso4",
  "Humble\nhttps://www.youtube.com/watch?v=TfChbdNLhOE",
  "7 AM Butterfly Doors\nhttps://www.youtube.com/watch?v=exyQ3iqEnYY",
  "Want To\nhttps://www.youtube.com/watch?v=WWAI8lk1gfI",
  "Preach\nhttps://www.youtube.com/watch?v=3Yf9Lzt8i3U",
  "1 AM\nhttps://www.youtube.com/watch?v=VIns1NIaERw",
  "Break the Bank\nhttps://www.youtube.com/watch?v=oKUCxMlicA8",
  "Long Time\nhttps://www.youtube.com/watch?v=_VtDJUy924A",
  "Hotel in Japan\nhttps://www.youtube.com/watch?v=ChCH53BAARE",
  "Whole Lotta Real(Tony Montana)\nhttps://www.youtube.com/watch?v=Km6u80mpvWo",
  "Illusion x Meh(That one tiktok song)\nhttps://www.youtube.com/watch?v=kZmZ-DvGXvM",
  "Choppa Stick\nhttps://www.youtube.com/watch?v=OnuUy-wE2k0",
  ]

#song list
#other songs list
songList = [
  "Don't - Bryson Tiller\nhttps://www.youtube.com/watch?v=d7cVLE4SaN0",
  "Range Brothers - Baby Keem ft. Kendrick Lamar\nhttps://www.youtube.com/watch?v=IkuBYRUwWdg",
  "Family Ties - Baby Keem ft. Kendrick Lamar\nhttps://www.youtube.com/watch?v=Drb3fRc5kZg",
  "Collard Greens - ScHoolboyQ ft. Kendrick Lamar\nhttps://www.youtube.com/watch?v=m61VNt0rM5s",
  "Moon - Kanye West\nhttps://www.youtube.com/watch?v=fMjasXiIhiQ",
  "Believe What I Say - Kanye West\nhttps://www.youtube.com/watch?v=Qp-O4eIUgf0",
  "Junya - Kanye West\nhttps://www.youtube.com/watch?v=uZET6hpfV-4",
  "Watermelon Hero - TisaKorean\nhttps://www.youtube.com/watch?v=xekg52pjoYU",
  "Industry Baby - Lil Nas X\nhttps://www.youtube.com/watch?v=eg-AwKRUFec",
  "Wesley's Theory - Kendrick Lamar\nhttps://www.youtube.com/watch?v=l9fN-8NjrvI",
  "Red Light Green Light - Dababy\nhttps://www.youtube.com/watch?v=jjBh9qhYGAE",
  "Thrax - ssgkobe\nhttps://www.youtube.com/watch?v=y4NVgllq_zY",
  "What You Need - Don Toliver\nhttps://www.youtube.com/watch?v=hLwkwJ9JCdc",
  "VIBEZ - Dababy\nhttps://www.youtube.com/watch?v=NBG3HF5l8jU",
  "Tell Em - Cochise ft. $not\nhttps://www.youtube.com/watch?v=eH_TOrddnZ0",
  "Ok - Lil Skieshttps://www.youtube.com/watch?v=t61Aozf5gnw",
  "444+222 - Lil Uzi Vert\nhttps://www.youtube.com/watch?v=EepkVbNveX0",
  "Same - whoispdp ft. Johnny Drama\nhttps://www.youtube.com/watch?v=gXkTkPRM_To",
  "Spaceship - Cochise\nhttps://www.youtube.com/watch?v=7XiIY6Hs4fU",
  "CAN'T SAY - Travis Scott\nhttps://www.youtube.com/watch?v=gpnQhbOMQDA",
  "BUTTERFLY EFFECT - Travis Scott\nhttps://www.youtube.com/watch?v=fdlbPYI8M_M",
  "sweet sweet - Travis Scott\nhttps://www.youtube.com/watch?v=vlFAZ1f8IIo",
  "Never - JID\nhttps://www.youtube.com/watch?v=01vZrReuV84",
  "5% TINT - Travis Scott\nhttps://www.youtube.com/watch?v=6SLD1ZQZ_4Y",
  "7 AM - Lil Uzi Vert\nhttps://www.youtube.com/watch?v=ixDvq80wZps",
  "HOLIDAY - Lil Nas X\nhttps://www.youtube.com/watch?v=lHm3AP0hCcg",
  "DIET_ - Denzel Curry ft. Kenny Beats\nhttps://www.youtube.com/watch?v=kK_dCZJbVT8",
  "10&2 - Koi\nhttps://www.youtube.com/watch?v=ltHFKElOnAs",
  "20 Min - Lil Uzi Vert\nhttps://www.youtube.com/watch?v=bnFa4Mq5PAM",
  "DOLLAZ ON MY HEAD - Gunna\nhttps://www.youtube.com/watch?v=lxZllACzsrU",
  "STARGAZING - Travis Scott\nhttps://www.youtube.com/watch?v=2a8PgqWrc_4",
  "Sauce It Up - Lil Uzi Vert\nhttps://www.youtube.com/watch?v=bncb3dm8K7g",
  "Two® - Lil Uzi Vert\nhttps://www.youtube.com/watch?v=Qg-JRPYbHXg",
  "Headlines - Drake\nhttps://www.youtube.com/watch?v=Sn3SUnL44w4",
  "Ps & Qs - Lil Uzi Vert\nhttps://www.youtube.com/watch?v=f_1uvkbDu_8",
  "Ransom - Lil Tecca\nhttps://www.youtube.com/watch?v=XLofd-v_Bas",
  "1400/999 Freestyle - Trippie Red and JuiceWRLD\nhttps://www.youtube.com/watch?v=3WnLTACoSfw",
  "GANG GANG - JACKBOYS, Sheck Wes\nhttps://www.youtube.com/watch?v=w9M7ydpcDSw",
  "Show Me Up - Lil Tecca\nhttps://www.youtube.com/watch?v=JQEr_8NrfTY",
  "Slay3r - Playboi Carti\nhttps://www.youtube.com/watch?v=a0DJDF0uSek",
]

ls = cartiList.extend(songList)

class songRater(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def getSong(ctx, song):
    if(songList.find(song) != -1):
      await ctx.send(ls[ls.index(song)])
    else:
      await ctx.send("Song not found in list!")

  @commands.command()
  async def getAllSongs(ctx):
    await ctx.send(ls)
    

def setup(client):
  client.add_cog(songRater(client))
