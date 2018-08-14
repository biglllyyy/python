import json
m = {
    'a': 1,
    'b': 2,
    'c ': 3,
    'd': 4

}
# print type(data)
#
# jsfile = json.dumps(data)
# print type(jsfile)
# print type(json.loads(jsfile))
# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(m, f)

# Reading data back
with open('data.json', 'r') as f:
    a = json.load(f)
    print a
