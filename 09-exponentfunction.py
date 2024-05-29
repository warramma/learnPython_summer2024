#5-29-24
#using for loops to create an exponent function

def exponent(base, power):
    answer = 1
    for exp in range(power):

        answer *= base

    print(answer)

base = float(input("Enter the base: "))
power = int(input("Enter the power: "))



exponent(base, power)