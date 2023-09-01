# dictionary

# Key-Value pairs

# contact_list = {
#     "jane": "07123456789"
# }
#
# contact_list["bob"] = "07987654321"
#
# contact_list["bob"] = "new number"
#
# # print(contact_list["jane"])
# # print(contact_list)
# # print(contact_list.keys()) # returns all keys available, useful for large dictionaries
# # print(contact_list.values()) # returns all the values in the dicts
# # print(contact_list.pop()) # will remove a certain value from the dict and requires its key
#
# print(contact_list.pop("jane"))
# print(contact_list)

contact_list = {
    "a": {
        "anne": "07182746371"
    },
    "b": {
        "bob": "07657463527"
    },
    "c": {
        "charles": "07818276453"
    }
}

print(contact_list['b'].keys()) # returns all available contacts under the 'b' section of the dict