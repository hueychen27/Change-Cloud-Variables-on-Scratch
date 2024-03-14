#!/bin/env python3
import os

os.system("pip install -U scratchattach --break-system-packages")

import scratchattach as scratch3
import json

f = open("config.json", "r")
conf=json.loads(f.read())
global username
global id
global forever
if conf["use"]==True:
    username = conf["username"]
    id=conf["sessionId"]
    forever=conf["forever"]
else:
    id=input("Input session id (See https://github.com/TimMcCool/scratchattach/wiki/Get-your-session-id to get cookie id): ")
    username=input("Input your Scratch username: ")
f.close()
project_id=input("Input project id: ")
conn = scratch3.CloudConnection(project_id = project_id, username=username, session_id=id)
print("Logged in!")
var_name=input("What variable name do you want to set?: ")
var_input=input("What do you want to set " + var_name + " to?: ")
if forever==True:
    while True:
        conn.set_var(var_name, var_input)
else:
    conn.set_var(var_name, var_input)