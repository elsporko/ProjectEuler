from collections import defaultdict

# Problem 5:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def prime_factors(num):
    factors = defaultdict(lambda:0)
    n = 2

    while (num != 1):
        while num % n == 0:
            factors[n] += 1
            num /= n
        n += 1
    return dict(factors)

factor_list={}

# Count and find all prime factors for the 
for i in range(1,20):
    # prime_factors returns a list of factors and the number of times they appear
    p=prime_factors(i)
    for f in p:
        try:
            if factor_list[f] < p[f]:
                factor_list[f] = p[f]
        except KeyError:
            factor_list[f] = p[f]

lcf=1
for i in factor_list:
    lcf = lcf * (i ** factor_list[i])

print ("Lowest common dividible number of 1-20: ", lcf)
