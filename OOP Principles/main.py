import customer
import employee
import random

if random.randint(0,1) == 0:
    my_person = customer.Customer('Jyoti', 'Suresh', 'Mumbai')
else:
    my_person = employee.Employee('Minato', 'Fujiwara', 'Marketing')
my_person.print()

# emp.print() # Polymorphism calling on employee
# cust.print() # Polymorphism calling on customer

