import requests

def BODServerCount(client, authtoken):
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
        requests.post(f"https://botsofdiscord.com/api/auth/stats/{botid}", headers=headers, data = payload)
        return f"{servers} {botid}"
    except:
        return False