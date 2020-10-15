import aiohttp

async def BODServerCount(client, authtoken):
    servers = len(client.guilds)
    botid = int(client.user.id)
    payload = "{\""
    payload += str(servers)
    payload += """\": 1500}"""
    headers = {
        'authorization': f'{authtoken}',
        'Content-Type': 'application/json'
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=f"https://botsofdiscord.com/api/auth/stats/{botid}", headers=headers, data=payload) as resp:
                return f"{servers} {botid}"
    except Exception as e:
        return e