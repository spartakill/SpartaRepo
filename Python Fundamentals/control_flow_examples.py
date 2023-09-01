# cinema age management

customer_age = 15

if customer_age <= 12:
    print('U, PG and 12 films are available')
elif customer_age <= 15:
    print('U, PG, 12, 15 films are available')
else:
    print('all films are available')

# chat bot example

time_of_day = 6

if time_of_day > 5 and time_of_day < 12:
    print('Good Morning')
elif time_of_day > 12 and time_of_day < 18:
    print('Good Afternoon')
else:
    print('Good Evening')