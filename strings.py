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

print(d)