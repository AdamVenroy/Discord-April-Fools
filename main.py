import random
import matplotlib.pyplot as plt
import numpy as np


def check_at_least_one(bucket):
    for i in bucket:
        if i == 0:
            return False
    
    return True

NUMBER_OF_SIMULATIONS = 100000
iteration_list = []
for _ in range(NUMBER_OF_SIMULATIONS):
    bucket = [0 for i in range(9)]
    number_of_iterations = 0
    while not check_at_least_one(bucket):
        number_of_iterations += 1
        i = random.choice(range(len(bucket)))
        bucket[i] += 1

    iteration_list.append(number_of_iterations)

print("Median", np.median(iteration_list))
print("Average", np.average(iteration_list))
plt.hist(iteration_list, 100)
plt.show()