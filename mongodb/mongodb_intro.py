import pymongo

client = pymongo.MongoClient()
db = client['starwars']

# Find the height of Darth Vader, only return results for the name and the height.

# characters = db.characters.find({"name":"Darth Vader"},{"name":1, "height":1, "_id":0})
# for character in characters:
#     print(character)

# Find all characters with yellow eyes, only return results for the names of the characters.

# characters = db.characters.find({"eye_color":"yellow"},{"name":1, "_id":0})
# for character in characters:
#     print(character)

# Find male characters. Limit your results to only show the first 3.

# characters = db.characters.find({"gender":"male"},{"name":1,"_id":0}).limit(3)
# for character in characters:
#     print(character)

# Find the names of all the humans whose homeworld is Alderaan.

# characters = db.characters.find({"homeworld.name":"Alderaan"},{"name":1, "_id":0})
# for character in characters:
#     print(character)

# characters = db.characters.find({"homeworld.name": {"$in": ["Alderaan", "Tatooine", "Mon Cala"]}}, {"name":1, "_id":0})
# for character in characters:
#     print(character)
