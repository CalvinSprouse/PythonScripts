import random
import sys

totalIterations = 0
numberOfSuccess = 0

while True:
    totalIterations += 1

    redVal = random.randint(0, 255)
    grnVal = random.randint(0, 255)
    bluVal = random.randint(0, 255)

    avgVal = int((redVal + grnVal + bluVal)/3)

    if avgVal == redVal or avgVal == grnVal or avgVal == bluVal:
        numberOfSuccess += 1

    sys.stdout.write("\rChance: {0}".format(format(numberOfSuccess/totalIterations * 100, '.5f')))
    sys.stdout.flush()
