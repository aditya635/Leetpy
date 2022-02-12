import json
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

f = open('test.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

conn = psycopg2.connect(
    host=os.environ['host'],
    database=os.environ['database'],
    user=os.environ['user'],
    password=os.environ['password'])


cursor = conn.cursor()

for leetobj in data["total_rank"]:
    print(f' username:{leetobj["username"]} and rank:{leetobj["rank"]}')
    query='''INSERT INTO leet(name,rank) VALUES (%s,%s)'''
    data = (leetobj["username"],leetobj["rank"])
    cursor.execute(query,data)

conn.commit()
conn.close()