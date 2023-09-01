# for loop

# iterates through given file or list

example_string = "test"

for character in example_string:
    print(character)

basket = ["eggs", "bread"]

for basket_item in basket:
    print(basket_item)

customers = {
    "name": "tess",
    "age": 28
}

for customer in customers.values(): # as its a dict you need to specify if you want values, if left blank it will product keys
    print(customer)