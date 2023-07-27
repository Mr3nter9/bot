from time import sleep;
import requests
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.sync import TelegramClient , functions , events
import asyncio
import random
import os
id='5229914714'
token='6183317549:AAGB5jAoTSGSc0M0Y_8WR7kEa7oYbyjshM0'
numb_s ='1'
user='dex34bot'
led=TelegramClient('Tshek2', 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
led.start()
uss='qwertyuioplkjhgfdsazxcvbnm1234567890'
rr='qwertyuioplkjhgfdsazxcvbnm'
@led.on(events.NewMessage(outgoing=True, pattern="B"))
async def spammer(event):
 await led.send_message('botfather', '/newbot')
 sleep(0.5)
 await led.send_message('botfather', 'Dex')
 while True:
  i = 0
  while True:
   i+=+1
   if i == 100:
    sleep(1.4)
    break

   while True:
    sleep(0.05)
    req = requests.get(f"https://t.me/{user}")
    if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
     await led.send_message('botfather', user)
     sleep(2)

    else:
     print(f"NOOO : {user}" +' '+ str(i))
   break


@led.on(events.NewMessage(pattern=r'^x', outgoing=True))
async def execute_script(event):
    x = 0
    while True:
        i=0
        while True:
            i += +1
            x += +1
            u = str(''.join((random.choice(uss) for i in range(2))))
            e = str(''.join((random.choice(rr) for i in range(1))))
            user = e + u + 'bot'
            if i == 100:
                sleep(1.4)
                break
            sleep(0.05)
            req = requests.get(f"https://t.me/{user}")
            if req.text.find(
                    'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
             try:
              take = await led(UpdateUsernameRequest(user))
              if take:
               requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text=« new hutting »
« UserName » : « @{user} »
---------------------------------
« attempts » : « {x} »
----------------------------------
« Save » : « Channel »
----------------------------------
« owner » :  @isiraqi »""")
             except Exception:
              pass
            else:
                print(f"NOOO : {user}" + ' ' + str(i) + " " + str(x))




led.run_until_disconnected()