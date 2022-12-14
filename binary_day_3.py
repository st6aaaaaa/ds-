'''You are given an array of characters letters that is sorted
in non-decreasing order, and a character target. There are at
least two different characters in letters.

Return the smallest character in letters that is lexicographically
greater than target. If such a character does not exist, return the
first character in letters.'''

'''Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically 
greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically 
greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically 
greater than 'z' so we return letters[0].'''


def nextGreatestLetter( letters, target: str) -> str:

    if target < letters[0] or target >= letters[len(letters) - 1]:
        return letters[0]

    low = 0
    high = len(letters) - 1

    while low <= high:
        mid = (low + high) // 2
        if target > letters[mid]:
            low = mid + 1
        elif target < letters[mid]:
            high = mid - 1
        else:
            if letters[mid] != letters[mid + 1]:
                return letters[mid + 1]
            else:
                while letters[mid] == letters[mid + 1]:
                    mid += 1
                return letters[mid + 1]

    return letters[low]



]
d= dict()
for i in s:
    if i not in d:
        d[i] = 1
    else :
        d[i]+=1
one_even = 0
n_1_odd = len(d) - 1
print(d)
for i in d :
    if d[i]%2 :
        one_even+=1
    else :
        n_1_odd -=1

if one_even > 1 or n_1_odd >1 :
    print('false')
else:
    print('true')
