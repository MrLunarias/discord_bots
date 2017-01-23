import discord
import asyncio
import requests

token = "TKN"

#leave for testing so we can run multiple at the same time -- adds a prefix to the trigger
trigPref = ""

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

#SCPBotCode

@client.event
async def on_message(message):
    trigMessage = message.content.lower()
    
    if trigMessage.startswith(trigPref + 'scp-'):
        await client.send_typing(message.channel)
        msg = message.content.split('-', 1)[1]
        
        if len(msg) <= 4 and len(msg) >= 3 and msg.isdigit():
            tmp_msg = await client.send_message(message.channel, '**Link:** http://www.scp-wiki.net/scp-' + msg + ' *Checking for existence...*')
            scp = requests.get('http://www.scp-wiki.net/scp-' + msg)
            if scp.status_code == 200:
#                await client.send_typing(message.channel)
                await client.edit_message(tmp_msg, '**Link:** http://www.scp-wiki.net/scp-' + msg + ' *SCP exists!*')

#               Someday images may get sent. Not today.
#                tree = BeautifulSoup(scp.text, "lxml")  
#                img_link = tree.find_all('div', class_="scp-image-block")[0].img.get('src')
#                await client.send_file(message.channel, img_link, filename='SCP-' + msg + '_img', content=None, tts=False)
                
            elif scp.status_code == 404:
                await client.edit_message(tmp_msg, '~~**Link:** http://www.scp-wiki.net/scp-' + msg + '~~ *SCP does not exist.*')
            else:
                await client.edit_message(tmp_msg,  '**Link:** http://www.scp-wiki.net/scp-' + msg + ' *Unable to determine if this SCP exists.*')

        else:
            await client.send_message(message.channel, 'SCP must be a 3 or 4 digit number. Example: `SCP-1175`')
#SarcasmBotCode
    elif trigMessage.startswith(trigPref + 'haha'):
        await client.send_message(message.channel, '^ sarcasm tbh')
#AyyLmaoBotCode
    elif trigMessage.startswith(trigPref + 'ayy'):
        await client.send_message(message.channel, 'lmao')

client.run(token)