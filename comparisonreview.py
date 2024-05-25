#5-24-2024
#review functions, comparision operators, and if-statements

#OBJECTIVE: return the MINIMUM number
def return_min(num1, num2, num3):
    if(num1 <= num2 and num1 <= num3):
        return num1
    elif(num2 <= num1 and num2 <= num3):
        return num2
    else:
        return num3

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
num3 = float(input('Enter the third number: '))

print('The minimum number is: ' + str(return_min(num1, num2, num3)))