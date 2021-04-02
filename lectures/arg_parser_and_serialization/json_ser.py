import json

with open('test.json', 'r') as f:
    data = json.load(f)

for user in data:
    user_id = user['_id']
    print(user_id)

with open('test.json', 'w') as f:
    json.dump(data, f, sort_keys=True)
