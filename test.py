import random
import time

from algorithms import *

n = 1000
print("n:", n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]

start_time = time.time()
result = max_diff(numbers)
end_time = time.time()

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")