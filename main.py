import random as r
import math
def calc_rand_sum():
    sum = 0
    number_of_num = 0
    while sum < 1:
        sum += r.random()
        number_of_num += 1

    return number_of_num





total = 0
iteration = 0
while True:
    total += calc_rand_sum()
    iteration += 1
    if iteration % 100000 == 0:
        print("nth Iteration: {}" .format(iteration))
        print("e approximation: {}" .format(total / iteration))
        print("delta from e: {}" .format(math.e - (total / iteration)))


