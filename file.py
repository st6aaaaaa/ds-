'''Given a string s, return true if a permutation of the string could form a
palindrome
 and false otherwise.'''
'''Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true'''


def canPermutePalindrome(s: str) -> bool:
    d = dict()
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    ev = 0
    od = len(d) - 1

    for i in d:
        if d[i] % 2:
            ev += 1
        else:
            od -= 1
    if ev > 1 or od > 1:
        return False
    return True
import collections as c

def func(s):
    d = c.Counter(s)
    cnt_od = 0
    for i in d:
        if d[i]%2 == 1:
            cnt_od+=1
        if cnt_od > 1 :
            return False
    return True
def foo(s):
    d = dict()
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(d)
    print( False if len([1 for i in d if d[i]%2==1]) > 1  else True )

def rrr(s):

    return ( False if len([1 for i in c.Counter(s) if c.Counter(s)[i]%2==1]) > 1 else True)


rrr('qweqwert')

'''Given a non-empty array of integers nums, every element appears 
twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity
 and use only constant extra space.
'''
def singleNumber(nums) -> int:
    res = 0
    for i in nums:
        res ^= i
    return res

def coin(n):
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        if mid * (mid + 1) / 2 > n:
            high = mid - 1
        elif mid * (mid + 1) / 2 < n:
            low = mid + 1
        else:
            return mid
    return high

def f2(a):
    return 1 if a&(a-1) else 0
def f1(a,b):
    return f2(a^b)


def number_of_bits(n):
    cnt = 0
    while n != 0:
        if n & 1:
            cnt += 1
        n >>=1
    return cnt
a = number_of_bits(255)
print(a)
a = 5
#print ( 1>>1 )