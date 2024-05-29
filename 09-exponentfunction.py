#5-29-24
#using for loops to create an exponent function

base = float(input("Enter the base: "))
power = int(input("Enter the power: "))

def exponent(base, power):
    answer = 1
    for exp in range(power):

        answer *= base

    print(answer)

#exponent(base, power)