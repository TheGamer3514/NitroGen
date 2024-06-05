#Check If Installed
try: 
    import os
    import requests  
except ImportError: 
    os.system("pip install requests")
try:
    import os
    import gamer3514
except ImportError:
    os.system("pip install gamer3514")
#import
import random
import string
import time
import os
import requests
from gamer3514 import randomstuff
web = False #Change this to True to enable the keep alive server
#start the gen
randomstuff.niceprint("Gamer's Nitro Generator\nDiscord: discord.gg/sillydev\nIf you like this tool give it a star on github!")
time.sleep(0.75)
randomstuff.niceprint("Starting The Gen...")
time.sleep(0.25)
randomstuff.niceprint("Gen Started. Enjoy!")
#gen codes
def gencode():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(19))

class Generator:
    def __init__(self):
        self.codes = []
        self.check()

    def check(self):
        while True:
            code = gencode()
            self.codes.append(code)
            response = requests.get(
                "https://discord.com/api/v7/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
            data = response.json()
            if data["message"] == 'Unknown Gift Code':
                randomstuff.niceprint("Invalid: " + code)
            elif data["message"] == 'The resource is being rate limited.' or 'You are being rate limited.':
                randomstuff.niceprint('Rate Limited: ' + code)
                randomstuff.niceprint('Waiting For Rate Limit To Go Away...')
                randomstuff.niceprint(data)
                time.sleep(int(data['retry_after'])/1000)
            else:
                randomstuff.niceprint("Working: " + code)
                file = open("workedcodes.txt", "a+")
                file.write("\n" + code)
#Keep Alive
if web == True:
    from keepalive import keep_alive
    keep_alive()
Generator()
