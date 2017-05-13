import praw
import config
import time
import datetime

def bot_login():
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = 'AnCapBot v0.1')
                    
    return r

def run_bot(r):
    global min
    global replyed_comments
    for comment in r.subreddit('test').comments(limit=100):
        if 'communism' and 'human nature' in comment.body:
            print 'Anarchokiddie found! ' + comment.id
            comment.reply('https://i.imgur.com/P55sPy0.jpg')
            
        else:
            time.sleep(10)
            run_bot(r)
    
r = bot_login()
run_bot(r)

