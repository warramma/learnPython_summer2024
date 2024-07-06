#7-6-24
#first ever test case
num1 = float(input('enter first number: '))
num1 = float(input('enter first number: '))

def getSum(num1, num2):
    return num1 + num2

def getDifference(num1, num2):
    return num1 - num2

def getProduct(num1, num2):
    return num1 * num2

def getQuotient(num1,num2):
    if(not(num1 == 0) and num2 == 0):
        return 'undefined'
    else:
        return num1 / num2

testCases = [
    (8, 2, 10, 6, 16, 4),
    (1, 0, 1, 1, 0, 'undefined')
]
def testSum():
    for i, (input1, input2, expectedsum, expecteddiff, expectedprod, expectedquot) in enumerate(testCases):
        sum = getSum(input1, input2)
        assert sum == expectedsum, f"Test case {i+1} failed: {input1} + {input2} = {expectedsum}"
    print('getSum passed!')

testSum()