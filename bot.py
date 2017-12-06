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
#present date/ loaded date
prdt=None
Today=None
Tomorrow=None
Yesterday=None
dt=None
dt_yes=None
dt_tom=None
today_error=None
tomorrow_error=None
yesterday_error=None

def on_chat_message(msg):
    valid_commands=["/whatscooking","/today","/tomorrow","yesterday"]
    global yesterday_error
    global tomorrow_error
    global today_error
    print("\n")
    pp.pprint(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if(content_type!="text"):
            print(content_type)
            reply='Sorry, But, I only accept text :-(\nType or Click "/ " to see available commands'
    else:
        global dt
        global dt_yes
        global dt_tom
        dt=datetime.datetime.fromtimestamp(msg["date"],tz=gmt5)
        ti=dt.time()
        print(ti)
        global prdt
        reply=dt.strftime("Today is %A, %d %b %Y\n\n")
        #date change
        if(prdt is None or prdt.date()!=dt.date()):
            tdt=datetime.timedelta(days=1)
            dt_yes=dt-tdt
            dt_tom=dt+tdt
            todayfile=dt.strftime("./menu/%d-%m-%Y.json")
            yesterdayfile=dt_yes.strftime("./menu/%d-%m-%Y.json")
            tomorrowfile=dt_tom.strftime("./menu/%d-%m-%Y.json")
            print("in date change")
            
            try:
                with open(todayfile) as json_data:
                    global Today 
                    Today = json.load(json_data)
                    json_data.close()
            except:
                today_error=True
            try:    
                with open(yesterdayfile) as json_data:
                    global Yesterday 
                    Yesterday= json.load(json_data)
                    json_data.close()
            except:
                yesterday_error=True
            try:
                with open(tomorrowfile) as json_data:
                    global Tomorrow 
                    Tomorrow= json.load(json_data)
                    json_data.close()
            except:
                tomorrow_error=True
        prdt=dt
        k=''
        t=msg['text']
        print(tomorrow_error)
        

        if(t=="/whatscooking" and not today_error):
            nextmeal=Today["breakfast"]
            reply1="Today's Breakfast:"
            if(ti.hour==9 and ti.minute>30 or ti.hour>9):
                nextmeal=Today["lunch"]
                reply1="Today's lunch:"
            if(ti.hour==13 and ti.minute>30 or ti.hour>13):
                nextmeal=Today["dinner"]
                reply1="Today's dinner:"
            if(ti.hour==20 and ti.minute>30 or ti.hour>20):
                nextmeal=Tomorrow["breakfast"]
                reply=dt_tom.strftime("Tomorrow is %A, %d %b %Y\n\n")
                reply1="Tomorrow's Breakfast:"
            k=json.dumps(nextmeal,indent=0);
            reply+=reply1

        elif(t=="/today" and not today_error):
            k="\nBreakfast:"+json.dumps(Today["breakfast"],indent=0)+"\nLunch:"+json.dumps(Today["lunch"],indent=0)+"\nDinner:"+json.dumps(Today["dinner"],indent=0)
            reply+="Today's menu-\n"

        elif(t=="/yesterday" and not yesterday_error):
            reply=dt_yes.strftime("Yesterday was %A, %d %b %Y\n\n")
            k="\nBreakfast:"+json.dumps(Yesterday["breakfast"],indent=0)+"\nLunch:"+json.dumps(Yesterday["lunch"],indent=0)+"\nDinner:"+json.dumps(Yesterday["dinner"],indent=0)
            reply+="Yesterday's menu- \n"

        elif(t=="/tomorrow" and not tomorrow_error):
            reply=dt_tom.strftime("Tomorrow is %A, %d %b %Y\n\n")
            k="\nBreakfast:"+json.dumps(Tomorrow["breakfast"],indent=0)+"\nLunch:"+json.dumps(Tomorrow["lunch"],indent=0)+"\nDinner:"+json.dumps(Tomorrow["dinner"],indent=0)
            reply+="Tomorrow's menu:\n"
        elif((today_error or tomorrow_error or yesterday_error) and t in valid_commands):
            print("in error")
            reply="Sorry! the bot is no longer being maintained due to less usage :-(\nIf you are interested in maintaining the bot write to :\ndiveshuttamchandani@gmail.com"
        else:
            reply='Sorry! the bot is no longer being maintained due to less usage :-(\nIf you are interested in maintaining the bot write to :\ndiveshuttamchandani@gmail.com'

        k=k.replace('{','')
        k=k.replace('}','')
        k=k.replace('"','')
        k=k.replace('[','')
        k=k.replace(']','')
        k=k.replace(',','\t')
        reply+=k
        
        if(t=="/start"):
            reply='Hi! So let us see what is being cooked.\nType or Click  "/ "  to see available commands'

    bot.sendMessage(chat_id,reply)


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message})
print('Listening ...')

while 1:
    time.sleep(1)
