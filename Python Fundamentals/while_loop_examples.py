# while loops

"""

Equality Operators

Operator|Meaning
==      | equal to
!=      | not equal to
>       | greater than
<       | less than
>=      | greater than or equal to
<=      | less than or equal to

"""

# loop_control = True
#
# while loop_control:
#     print("I am a loop") # it will keep printing as its always going to be true, this is a danger of while loops and
#     # they can return infinite results

counter = 0

while counter < 10:
    if counter % 2 == 0:
        print(counter)
    else:
        print("odd number")
    counter += 1 # counter = counter + 1

