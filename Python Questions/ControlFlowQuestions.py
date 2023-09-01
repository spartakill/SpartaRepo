print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print(x[:5])


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for num in x:
    if num % 2 == 0:
        print(num, end=" ") # end =" " tells python to separate the values by a space not a new line


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for num in x[:5]:
    if num % 2 == 0:
        print(num, end=" ")

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
for name in names:
    first_letters = [name[0]]
    print(first_letters, end=" ")


print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

for name in names:
    i = [name.index(" ")]
    print(i, end=" ")



print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

for name in names:
    initials = name.split(" ")
    first_and_last_initials = [initials[0][0], initials[1][0]]
    print(first_and_last_initials, end=" ")
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

# A3a:
for l in list_of_lists:
        if len(l) == len(set(l)):
            new_list = [l]
            print(new_list)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

game_active = True

while game_active:
    number = int(input('\n Enter a number: '))
    flag = 1
    if number == 100:
        print('well done, you entered 100 correctly')
        game_active = False
    elif number > 100:
        print('too large, go down')
    elif number < 100:
        print('too small, go up')
    for i in range(2, int(number/2)):
        if number%i == 0:
            flag=0
            break

    if flag == 1 and number >= 2:
        print("prime")
    else:
        print("not prime")
print("Here is the number you guessed: ", number)

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:


