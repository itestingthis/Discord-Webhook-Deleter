# Discord Webhook Deleter

import requests

webhookstartswith = "https://discord.com/api/webhooks/" 

webHook = input("Webhook URL : ")

if webhookstartswith not in webHook:
    print("Invalid Webhook URL")
    input("Press Enter to exit...")
else:
    print("Deleting Webhook...")
    requests.delete(webHook)
    print("Webhook Deleted")
    input("Press Enter to exit...")
#Lol, I made this in like 2 minutes, don't judge me :D
#py3lxx2
