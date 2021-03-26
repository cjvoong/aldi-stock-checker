import json, requests, time

class Item:
    def __init__(self,id,name):
        self.name=name
        self.id=id


url='https://www.aldi.co.uk/api/product/availability/710081460879600'
full_url='https://www.aldi.co.uk/gardenline-kamado-ceramic-egg-bbq/p/710081460879600'
headers={'authority': 'www.argos.co.uk','x-newrelic-id': 'VQEPU15SARAGV1hVDgMBUVY=','user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML,     like Gecko) Chrome/83.0.4103.97 Safari/537.36','content-type': 'application/json','accept': '*/*','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.argos.co.uk/product/6014179?clickSR=slp:term:weights:8:39:1','accept-language': 'en-US,en;q=0.9'}

slackurl='YOUR SLACK URL'

try:
    startmsg='{\'text\':\'started looking for aldi stock...\'}'
    requests.post(slackurl,headers={'content-type':'application/json'},data=startmsg)
    for x in range(10000):
        try: 
            print('looking for kamado bbq')
            r=requests.get(url,headers=headers)
            y=json.loads(r.text)
            found=0
            print(y["availabilityPanel"])
            if ("data-purchase-disabled=\"true\"" in y["availabilityPanel"]):            
                print("Still out of stock")
            else:
                instockmsg="{'text':'Its in stock! " + full_url + "'}"
                print("Its in stock!")
                requests.post(slackurl,headers={'content-type':'application/json'},data=instockmsg)   
        except:
            print("An error occurred")
        finally:
            print("trying again in 1 mins...")
            time.sleep(60)
finally: 
    exitmsg='{\'text\':\'exiting script...\'}'
    requests.post(slackurl,headers={'content-type':'application/json'},data=exitmsg)
    print("exiting script...")
