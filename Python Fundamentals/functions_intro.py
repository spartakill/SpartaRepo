# functions

# DRY = Don't Repeat Yourself

# Creates a function outside of code, to be used in several other pieces of code

# e.g.

def full_name(first_name, last_name):
    return first_name + ' ' + last_name

def print_name(data_type):
    print(data_type)

print(full_name("Killian", "Hughes"))

print_name(full_name("Killian", "Hughes"))