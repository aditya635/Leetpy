import requests
import json
import math 
import os
from time import sleep
import psycopg2
from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(
    host=os.environ['host'],
    database=os.environ['database'],
    user=os.environ['user'],
    password=os.environ['password'])


cursor = conn.cursor()

print ("Please tell which contest number you want :")
m = int(input())
text = requests.get(f"https://leetcode.com/contest/api/ranking/weekly-contest-{m}/?pagination=1&region=india")
data = text.json()
pages = math.ceil(data['user_num']/25)
current = 0
for i in range(1,pages+1):
    text = requests.get(f"https://leetcode.com/contest/api/ranking/weekly-contest-{m}/?pagination={i}&region=india")
    info = text.json()
    
    for leetobj in info["total_rank"]:
        query='''INSERT INTO leet(name,rank) VALUES (%s,%s)'''
        data = (leetobj["username"],leetobj["rank"]+1)
        cursor.execute(query,data)
    conn.commit()
    current+=1
    if( current % 10 == 0):
        print(f"Well {current} requests has been made")
        sleep(1)
    

conn.close()

