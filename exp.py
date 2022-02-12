import json
import psycopg2,requests
import os
from dotenv import load_dotenv
load_dotenv()

data = requests.get(f"https://leetcode.com/contest/api/ranking/weekly-contest-279/?pagination=1&region=india")
data=data.json()
print(data)
for leetobj in data["total_rank"]:
    print(f' username:{leetobj["username"]} and rank:{leetobj["rank"]}')
    
