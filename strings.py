'''Given a string s consisting of words and spaces,
return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.'''


def lengthOfLastWord(s: str) -> int:
    ##################  FIRST SOLUTION
    cnt = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            cnt += 1
        elif cnt > 0:
            return cnt

    return cnt

    #########################   SECOND SOLUTION
    s = s.strip().replace(' ', '9')
    ind = s.rfind('9')
    if ind == -1:
        return len(s)
    return len(s[ind + 1:])

'''Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

'''
import collections as c
def firstUniqChar( s: str) -> int:
    ans = c.Counter(s)
    for el in s:
        if ans[el] == 1:
            return s.index(el)
    return -1

d = c.deque()
a = [1,2,3,4,5]
for i,el in enumerate(a):
    if i == 3 :
        d.append((el,i))
    else :
        d.append(el)

'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.'''

import collections as c
def groupAnagrams(strs):
    d = c.defaultdict(list)

    for string in strs:
        tmp = ''.join(sorted(string))
        d[tmp].append(string)

    return list(d.values())


def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n - 1) + fib_without_cache(n - 2)


def pascal(i,j):
    if j==0 or i==0 or i==j:
        return 1
    return pascal(i-1,j) + pascal(i-1,j-1)

from functools import lru_cache

@lru_cache(maxsize= None)
def pascal_lru(i,j):
    if j==0 or i==0 or i==j:
        return 1
    return pascal(i-1,j) + pascal(i-1,j-1)


import time
#
# beg=time.time()
# res = pascal(32,25)
# beg2 = time.time()
# print(res , '  diff ',beg2 - beg )

arr = [[72,98],[62,27],[32,7],[71,4],[25,19],[91,30],[52,73],[10,9],[99,71],[47,22],[19,30],[80,63],[18,15],[48,17],[77,16],[46,27],[66,87],[55,84],[65,38],[30,9],[50,42],[100,60],[75,73],[98,53],[22,80],[41,61],[37,47],[95,8],[51,81],[78,79],[57,95]]

arr.sort(key = lambda x : x[0])
print(arr)

x = []
y = []
for el in arr :
    x.append(el[0])
    y.append(el[1])

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

