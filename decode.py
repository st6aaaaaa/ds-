'''Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the
encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces,
square brackets are well-formed, etc. Furthermore, you may assume that the original
data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.'''

'''Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"'''

import re

def func(s):
    if s=='':
        return s
    if '[' not in s:
        return s

    i_o_b = s.rfind('[')
    i_c_b= s.find(']',i_o_b)

    a = int(s[i_o_b-1])
    cnt = i_o_b - 2
    try:
        if type(int(s[i_o_b - 2])) == int:
            a += int(s[i_o_b-2])*10
            cnt-=1
            try:
                if type(int(s[i_o_b - 3])) == int:
                    a += int(s[i_o_b - 3]) * 100
                    cnt -= 1
            except:
                pass
    except :
        pass



    s = s[:cnt+1]+a*s[i_o_b+1:i_c_b]+s[i_c_b+1:]
    return func(s)
#a=func("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")


def decodeString(s: str) -> str:

    stack = []

    for i in s:
        if i != ']':
            stack.append(i)
        else:
            a = stack.pop()
            res = ''

            while a != '[':
                res += a[::-1]
                a = stack.pop()

            d = stack.pop()
            t = int(d)
            power = 1

            while stack:
                d = stack.pop()
                if d.isdigit():

                    t += int(d) * 10 ** power

                    power += 1
                else:
                    stack.append(d)
                    break

            r = t * res[::-1]
            stack.append(r)
    res = ''.join(stack)
    return res

decodeString("3[a]2[bc]")