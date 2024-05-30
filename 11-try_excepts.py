#5-30-24

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:  #specify exception type for more specific exception
    print('invalid')