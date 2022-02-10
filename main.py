import requests
import json

print ("Please tell which contest number you want :")
m = int(input())
text = requests.get(f"https://leetcode.com/contest/api/ranking/weekly-contest-{m}/?pagination=1")
print(text.json())
with open ('test.json', 'w') as json_file:
    json.dump(text.json(), json_file)
