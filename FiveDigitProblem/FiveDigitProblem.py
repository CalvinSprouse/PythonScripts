import random
import sys

number = [0, 0, 0, 0, 0]
correctNums = []


def isCorrect(numbers):
    if numbers[3] == (numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]) / 4:
        if numbers[1] == numbers[0] * 2:
            if numbers[2] > numbers[0] \
                    and numbers[2] > numbers[1] \
                    and numbers[2] > numbers[3] \
                    and numbers[2] > numbers[4]:
                if numbers[4] == numbers[0] + numbers[1]:
                    return True
    return False
    
def arrayToString(array):
    toReturn = ""
    for item in array:
        toReturn += str(item)
    return toReturn


while True:
    while not isCorrect(number) and not correctNums.__contains__(number):
        number[0] = random.randint(2, 9)
        number[1] = random.randint(2, 9)
        number[2] = random.randint(2, 9)
        number[3] = random.randint(2, 9)
        number[4] = random.randint(2, 9)

        sys.stdout.write("\rCurrent Num: " + str(arrayToString(number)) + "\t\tIs Correct: " + str(isCorrect(numbers=number)))
        sys.stdout.flush()

    if not correctNums.__contains__(number):
        print("\n")
        correctNums.append(number)
    number = [0, 0, 0, 0, 0]
