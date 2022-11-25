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