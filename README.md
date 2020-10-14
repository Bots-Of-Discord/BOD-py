# The Bots Of Discord Python API
Keep in mind that this is a beta API. Here's an example of how to use this.

```import discord, main
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(main.BODServerCount(client, 'AuthTokenHere'))

client.run("NzQyNDUwOTYyMzQ5ODE3OTU4.XzGTVw.gfCbzoOv5ZEJE_z2PZVYrqif2pA")```
