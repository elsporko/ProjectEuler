# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

import math

def is_prime(n):

    if n < 2:
        return False
 
    for p in range (2, int(math.sqrt(n) +1)):
        if n%p == 0:
            return False
    return True

pr = 1
pr_count = 1
while pr_count < 10002:
    if is_prime(pr):
        #print("{} is prime. Number: {}".format(pr, pr_count))
        print("Found prime({}): {}".format(pr_count, pr))
        pr_count += 1
    pr += 1

print ("10001 prime: ", pr)
