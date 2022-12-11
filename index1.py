class book:
    def __init__(self,author,name):
        self.name = name
        self.author = author
    def __repr__(self):
        return self.name+ ' ' + self.author



# import re
#
# ans = re.search(r'[+-]?\d+','111')
#
# print('123456'[-1:2])
#

def binarysearch(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high :
        mid = (low + high )//2
        if nums[mid] == target :
            return mid
        if nums[mid] < target :
            low = mid + 1
        else :
            high = mid - 1
    return low



s='qweqwee123qwe'
pat = r'\d{3}[a-z]'

ranks = [13,2,2,3,1,9]
import collections as c

import math


# A function to print all prime factors of
# a given number n
def primeFactors(n):
    # Print the number of two\'s that divide n
    while n % 2 == 0:
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            print(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2

import collections as c

r1 = c.Counter("a")
r2 = c.Counter("b")

print(list(zip(r1.keys(),r2.keys())))
