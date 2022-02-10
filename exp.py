import json

f = open('test.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

for leetobj in data["total_rank"]:
    print(f' username:{leetobj["username"]} and rank:{leetobj["rank"]}')