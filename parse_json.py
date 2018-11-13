import json
from pprint import pprint

with open('/var/tmp/json.txt') as f:
    data = json.load(f)
    #data = (f)

pprint(data)
