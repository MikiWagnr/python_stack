'''
- variable declaration
- log statement
- type check
- length check
- comment
    - single line
    - multiline
- Data Types
    - Primitive
        - Boolean
        - Numbers
        - Strings
    - Composite
        - List 
            - initialize
            - access value
            - change value
            - add value
            - delete value
        - Tuples
            - initialize
            - access value
            - change value
            - add value
            - delete value
        - Dictionary
            - initialize
            - access value
            - change value
            - add value
            - delete value
- conditional
    - if
    - else if
    - else
- for loop
    - start
    - stop
    - increment
    - break
    - continue
    - sequence
- while loop
    - start
    - stop
    - increment
- function
    - parameter
    - argument
    - return

* Bonus: Errors

- NameError: name <variable name> is not defined
- TypeError: 'tuple' object does not support item assignment
- KeyError: 'favorite_team'
- IndexError: list index out of range
- IndentationError: unexpected indent
- AttributeError: 'tuple' object has no attribute 'pop'
- AttributeError: 'tuple' object has no attribute 'append'
- Tuples
    - change value
    - add value
    - delete value
    '''

num1 = 42 #variable declarations initialize primitive data type integer
num2 = 2.3 #variable declaratioin initialize primitive data type float number
boolean = True #variable declaration initialize primitive data type boolean 
string = 'Hello World' #variable declaration initialize primitive data type string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration initialize composite data type list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration initialize composite data type dictionary 
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration initialize composite data type tuple
print(type(fruit)) #log statement (type check(composite data type tuple))
print(pizza_toppings[1]) #log statement(composite data type list[access value])
pizza_toppings.append('Mushrooms') #composite data type lists.add value(primitive dasta type string)
print(person['name']) #log statement(composite data type dictionary[access value])
person['name'] = 'George' #composite data type dictionary[access value] change value primitive data type string
person['eye_color'] = 'blue' #composite data type dictionary[access value] change value primitive data type string
print(fruit[2]) #log statement(composite data type tuple[access value])

if num1 > 45: #conditional if statement
    print("It's greater") #log statement(primitive data type string)
else: #conditional else statement
    print("It's lower") #log statement(primitive datatype string)

if len(string) < 5: #contitional if statement length check(primitive data type string)
    print("It's a short word!") #log statement(primitive data type string)
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry') #- AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #- AttributeError: 'tuple' object has no attribute 'pop'