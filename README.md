# MessMenuBot
a [telegram](http://t.me) bot for displaying mess menu. Bot's Url- [t.me/messmenubot](https://t.me/messmenubot)  
  
**The bot is no longer being maintained due to less usage.  
However if you are interested in maintaining the bot, write to : diveshuttamchandani@gmail.com**  

### NOTE:
Menu is prepared fortnightly -- on 1st and 15th of each month so it may take some time for the menu to be updated here and there may be a couple of days around these dates when bot doesn't have the menu availible. Though the menu is generated using scripts and is out as soon as the excel file is out.

### requirements:
  [telepot](http://telepot.readthedocs.io/en/latest/)  
    
### run:  
  python3 bot.py token  
  replace token by the token string that you get from bot father  
    
  on the server using a Environmental variable that stores token and calling it from Procfile  
  
### availible commands:  
  /whatscooking   (menu for current/next meal)  
  /today          (today's complete menu)  
  /tomorrow      (tomorrow's complete menu)  
  /yesterday      (yesterday's complete menu)  
  
Menu is rendered from date-wise json files in menu folder.All three required menu files(today's,yesterday's,tomorrows's) are loaded into memory once a day so not much need of a DBMS. 
  
### extracting menu from xlsx to json:  
  1)  copy the xlsx menu file to the extractmenu folder.  
  2)  update arg.json with the row number of start and end of each meal.(base 1 row no i.e the row no displayed in the excel sheet)  
  3)  run menuextract.py (this creates the json files in folder ../menu and also prints the arguments to the screen for reference)  
  Note: only one file extracted at a time
