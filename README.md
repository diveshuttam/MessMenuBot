# MessMenuBot
a [telegram](t.me) bot for displaying mess menu. Bot's Url- [t.me/messmenubot](t.me/messmenubot)


### requirements:
  [telepot](http://telepot.readthedocs.io/en/latest/)  
    
### run:  
  python3 bot.py token  
  replace token by the token string that you get from bot father  
    
  in server using a Environmental variable that stores token and calling it from Procfile  
  
### availible commands:  
  /whatscooking   (menu for current/next meal)  
  /today          (today's complete menu)  
  /tomorrow      (tomorrow's complete menu)  
  /yesterday      (yesterday's complete menu)  
  
Menu is rendered from date-wise json files in menu folder.All three required menu files(today's,yesterday's,tomorrows's) are loaded into memory once a day so not much need of a DBMS. 
