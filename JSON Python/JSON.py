import json

# course = {"name":"Data 249","trainer":"Paula"}

# print(type(course))
# print(course)
#
# course_json_str = json.dumps(course) # writes json to a python string
# print(type(course_json_str))
# print(course_json_str)

# with open("new_json_data.json", "w") as jsonfile:
#     json.dump(course, jsonfile) # writes json data to file

# with open("new_json_data.json") as jsonfile:
#     course_file = json.load(jsonfile) # turns JSON encoded data into a python dictionary
#     print(course_file['name'])
#     print(type(course_file))

# loads reverts dumps, where dumps converts dict to json string, load converts json string to dict

import requests

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/SM25JS")
#
# print(post_codes_req.headers) # returns headers
# print(post_codes_req.json()) # returns a python dictionary
# print(post_codes_req.content) # contents
# print(type(post_codes_req.json())) # type

headers = {'Content-Type': 'application/json'}
json_data = json.dumps({'postcodes' : ["PR3 0SG", "M45 6GN", "EX165BL"]})

post_codes_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_data)

# print(type(post_codes_req.json()))
# print(post_codes_req.json())
print(post_codes_req.json()['result'][0]) # return the first list within the dictionary
print(post_codes_req.json()['result'][0]['result']['country']) # returns the country in first list
