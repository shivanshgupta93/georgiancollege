'''
For the JSON file get a list of Keys and print them. Then print the last 5 JSON calEvent Objects 
'''
import json

with open('festivals-and-events-json-feed.json') as json_file:
    json_data = json.load(json_file)

for key in json_data[0].get('calEvent'):
    print(key)

count = 6    
    
data_len = len(json_data)

json_data = json_data[data_len-5:data_len]

for item in json_data:
    count -= 1
    print('calEvent No: %s' %(data_len - count))
    print(item)

