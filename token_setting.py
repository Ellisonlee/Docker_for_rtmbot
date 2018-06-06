#!/usr/bin/python 
# coding: UTF-8
import os
token = os.getenv("SLACK_TOKEN", "xoxb-111111111111111-xxxxxxxxxxxxxxxxxxxxxxxxxx")
with open('temp.conf','r') as f:
    s = f.read()
    s = s.replace('BOT_TOKEN', token);
 
f = open("rtmbot.conf", 'w')
f.write(s) 
f.close()
