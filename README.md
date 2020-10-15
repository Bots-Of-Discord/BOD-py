# The Bots Of Discord Python API
Keep in mind that this is a beta API. Here's an example of how to use this.

```
import discord, BOD
from discord.ext import commands

client = commands.Bot(command_prefix='command prefix')

@client.event
async def on_ready():
    print(await BOD.BODServerCount(client, 'AuthTokenHere'))

client.run("Discord Bot Token")
```