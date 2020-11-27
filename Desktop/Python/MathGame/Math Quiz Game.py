from random import randint

def calculateAnswer(left,right,operator):
    if operator == "+":
        return left + right
    
    if operator == "-":
        return left - right

    if operator == "*":
        return left * right

    if operator == "/":
        return left / right
    if operator == "^":
        x = 0
        total = 1
        while x < right:
            total *= left
            x+=1
        return total           
    raise Exception("Unknown Operator")


def generate(lowerbound, upperbound):
    left = randint(lowerbound,upperbound)
    right = randint(lowerbound,upperbound)
    ops = "/*-+^"
    opIndex = randint(0,len(ops)-1)
    operator = ops[opIndex]
    while (right == 0 and operator == "/"):
        right = randint(lowerbound,upperbound)

    return left, right, operator


def float_tolerance(user, correct, tolerance = 0.01):
    difference = abs(float(user) - float(correct))
    return difference <= tolerance
    

totalqs = int(input ("How many questions would you like to answer?: "))
lower = int(input("What is the lowest number you would like to deal with?: "))
higher = int(input("What is the highest number you would like to deal with?: "))
correct = 0
for i in range(totalqs):
    question = generate(lower,higher)
    answer = round(calculateAnswer(question[0],question[1],question[2]), 2)

    playerans = input("{0} {2} {1} = ".format(question[0],question[1],question[2]))  

    if (float_tolerance(playerans,answer)):
        print("Correct")
        correct += 1
    else: 
        print("Nope not correct :( the answer is: " + str(answer))
print("Congrats, you got {} out of {} correct!".format(correct,totalqs))
