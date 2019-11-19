import sys
import random
import time


def randomRoll(targetNum: int):
    number = 0
    startingTime = time.time()
    while (number is not targetNum):
        number = random.randint(0, targetNum)
    return time.time()-startingTime

longestTime = 0
longestIteration = 0
iterations = 0
try:
    while (True):
        # time.sleep(0.05)
        currentTime = randomRoll(100)
        if (currentTime > longestTime):
            longestIteration = iterations
            longestTime = currentTime
        iterations += 1
        sys.stdout.write("\rIterations: {iteration}\tLongest Time (Iteration {longestIteration}): {time}"
            .format(iteration=iterations, longestIteration=longestIteration, time=longestTime))
        sys.stdout.flush()
except KeyboardInterrupt as ignored:
    exit()
