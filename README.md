# The Bots Of Discord Python API
Keep in mind that this is a beta API. Here's an example of how to use this.

```
import discord, BOD
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(BOD.BODServerCount(client, 'AuthTokenHere'))

client.run("Discord Bot Token")
```
You'd get this package by downloading the `BOD.py` file and putting it in the same directory. Import BOD, then do BOD.BOTServerCount(client, 'auth token here') or if you use bot, BOD.BOTServerCount(bot, 'auth token here')
