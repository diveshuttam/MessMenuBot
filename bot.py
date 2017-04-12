import sys
import time
import datetime
import telepot
import pprint
import json

class GMT5(datetime.tzinfo): 
    def utcoffset(self,dt):
        return datetime.timedelta(hours=5,minutes=30)
    def tzname(self,dt):
        return "GMT +5:30 (IST)"
    def dst(self,dt):
        return datetime.timedelta(0)

gmt5 = GMT5()

pp = pprint.PrettyPrinter(indent=4)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # pp.pprint(msg)
    print(telepot.glance(msg))
    if(content_type!="text"):
            reply='Sorry, But, I only accept text :-(\nType or Click "/ " to see availible commands'
    else:
        dt=datetime.datetime.fromtimestamp(msg["date"],tz=gmt5)
        #dt=dt.astimezone()
        ti=dt.time()
        #print(msg["date"])
        print(ti)

        reply=dt.strftime("Today is %A, %d %B %Y\n\n")

        with open('./today.json') as json_data:
            Today = json.load(json_data)
            json_data.close()
        with open('./yesterday.json') as json_data:
            Yesterday = json.load(json_data)
            json_data.close()
        with open('./tomorrow.json') as json_data:
            Tomorrow = json.load(json_data)
            json_data.close()

        k=''

        nextmeal=Today["breakfast"]
        reply1="Today's Breakfast:\n"
        if(ti.hour==9 and ti.minute>30 or ti.hour>9):
            nextmeal=Today["lunch"]
            reply1="Today's lunch:\n"
        if(ti.hour==13 and ti.minute>30 or ti.hour>13):
            nextmeal=Today["dinner"]
            reply1="Today's dinner:\n"
        if(ti.hour==20 and ti.minute>30 or ti.hour>20):
            nextmeal=Tomorrow["breakfast"]
            reply1="Tomorrow's Breakfast:\n"

        t=msg['text']

        if(t=="/whatscooking"):
            k=json.dumps(nextmeal);
            reply+=reply1

        elif(t=="/today"):
            k=json.dumps(Today,indent=0)
            reply+="Today's menu-\n"

        elif(t=="/yesterday"):
            k=json.dumps(Yesterday,indent=0)
            reply+="Yesterday's menu- \n"

        elif(t=="/tomorrow"):
            k=json.dumps(Tomorrow,indent=0)
            reply+="Tomorrow's menu:\n"

        else:
            reply='That'+"'s "+ 'Greek to me :-(\nType or Click "/ " to see availible commands'

        k=k.replace('{','')
        k=k.replace('}','')
        k=k.replace('"','')
        k=k.replace('[','')
        k=k.replace(']','')
        k=k.replace(',','\t')
        reply+=k
        
        if(t=="/start"):
            reply='Hi! So let us see what is being cooked.\nType or Click  "/ "  to see availible commands'

    bot.sendMessage(chat_id,reply)


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message})
print('Listening ...')

while 1:
    time.sleep(10)
