# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

s = lambda x: x**2
square_of_sums = s(sum(range(1,101)))

print ("square_of_sums: ", square_of_sums)

sum_of_squares = sum(map(s, range(1,101)))
print ("sum_of_squares: ", sum_of_squares)

print ("Difference: ", square_of_sums - sum_of_squares)
