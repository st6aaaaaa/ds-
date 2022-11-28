def from_dec_to_bin(a):
    res = []
    while a > 0:
        rem = a % 2
        res.append(str(rem))
        a = a // 2
    res.reverse()
    return ''.join(res)


'''You are given two 0-indexed arrays, nums1 and nums2, 
consisting of non-negative integers. There exists another array, 
nums3, which contains the bitwise XOR of all pairings of integers 
between nums1 and nums2 (every integer in nums1 is paired with every 
integer in nums2 exactly once).
Return the bitwise XOR of all integers in nums3.'''

'''Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:

A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].

The bitwise XOR of all these numbers is 13, so we return 13.'''


def func(nums1,nums2):
    res_b = 0
    res = 0

    for j in nums2:
        res_b ^= j

    if len(nums2) % 2 == 0:
        for i in nums1:
            res ^= res_b
    else:
        for a in nums1:
            res = res ^ a ^ res_b
    return res

def func(n,x):
    if n == 1:
        return x
    if n%2 == 0 :
        return func(n//2,x)**2
    else :
        return x*func(n//2,x)**2



'''You are given an integer array arr. Sort the integers in the array 
in ascending order by the number of 1's in their binary representation 
and in case of two or more integers have the same number of 1's you 
have to sort them in ascending order.

Return the array after sorting it.

Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
Example 2:

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, 
you should just sort them in ascending order.'''


def number_of_bits(n):
    cnt = 0
    while n:
        if n & 1:
            cnt += 1
        n >>= 1
    return cnt

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    barrier = number_of_bits(arr[0])
    l = [a for a in arr if number_of_bits(a) < barrier]
    m = [a for a in arr if number_of_bits(a) == barrier]
    r = [a for a in arr if number_of_bits(a) > barrier]
    return quicksort(l) + sorted(m) + quicksort(r)

#arr = [1024,512,256,128,64,32,16,8,4,2,1]
#arr = quicksort(arr)



##################################

#second solution

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    l = merge_sort(arr[:len(arr) // 2])
    r = merge_sort(arr[len(arr) // 2:])

    return merge(l, r)


def merge(a, b):
    left_cursor = 0
    right_cursor = 0
    res = []
    while left_cursor < len(a) and right_cursor < len(b):
        if number_of_bits(a[left_cursor]) < number_of_bits(b[right_cursor]):
            res.append(a[left_cursor])
            left_cursor += 1
        elif number_of_bits(a[left_cursor]) > number_of_bits(b[right_cursor]):
            res.append(b[right_cursor])
            right_cursor += 1
        else:
            if a[left_cursor] <= b[right_cursor]:
                res.append(a[left_cursor])
                left_cursor += 1
            else:
                res.append(b[right_cursor])
                right_cursor += 1
    res.extend(a[left_cursor:])
    res.extend(b[right_cursor:])
    return res



def func(arr):
    return merge_sort(arr)


def convert_list_int(nums):
    power =0
    res = 0
    for i in range(len(nums)-1,-1,-1):
        res += nums[i]*2**power
        power+=1
    return res
[0, 1, 1, 1, 1, 1, 1, 1]

def binary(n):
    if n==1 :
        return [0]
    if n==0 :
        return [1]
    else :
        return binary(n//2) + ( [0] if n % 2 else [1] )



def travelling(arr,res=[]):
    if len(arr) == 1:
        res.append(arr[0])
        return res
    else :
        res.append(arr[0])
        print('hello ',end='')
        print(res)
        travelling(arr[1:],res)


'''You are given a string allowed consisting of distinct 
characters and an array of strings words. A string is consistent 
if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.'''


def countConsistentStrings( allowed: str, words) -> int:
    cnt = 0
    flag = False

    for word in words:
        s = set(word)
        for i in s:
            if i not in allowed:
                flag = True
                break
        if flag == False:
            cnt += 1

        if flag:
            flag = False

    return cnt

'''A bit flip of a number x is choosing a bit in the binary representation of x 
and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and 
we may choose any bit (including any leading zeros not shown) and flip it. 
We can flip the first bit from the right to get 110, 
flip the second bit from the right to get 101, flip the fifth bit 
from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit 
flips to convert start to goal.

 

Example 1:

Input: start = 10, goal = 7
Output: 3
Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. 
We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 1010 -> 1011.
- Flip the third bit from the right: 1011 -> 1111.
- Flip the fourth bit from the right: 1111 -> 0111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.
Example 2:

Input: start = 3, goal = 4
Output: 3
Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. 
We can convert 3 to 4 in 3 steps:
- Flip the first bit from the right: 011 -> 010.
- Flip the second bit from the right: 010 -> 000.
- Flip the third bit from the right: 000 -> 100.
It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.'''


def minBitFlips(start: int, goal: int) -> int:
    start = bin(start)[2:]
    goal = bin(goal)[2:]

    maximum = max(len(start), len(goal))

    start = start.zfill(maximum)
    goal = goal.zfill(maximum)

    cnt = 0

    for i in range(maximum):
        if start[i] != goal[i]:
            cnt += 1
    return cnt


def inverse(n):
    s =''
    for i in n:
        if i=='1':
            s+='0'
        else :
            s+='1'
    return s
def function(n):
    print(hex(n)[2:])
    a = bin(n)[2:]
    print(a, ' ', int(a,16))
    a = inverse(a)
    print(a, ' ',int(a,16),' ',int(a,2))

'''Given a positive integer, check whether it has alternating bits: 
namely, if two adjacent bits will always have different values.

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.'''


def hasAlternatingBits(n):
    #return not ('00' in bin(n) or '11' in bin(n))

    while n:
        b1 = n & 1
        n >>= 1
        b2 = n & 1
        if b1 == b2:
            return False
    return True


'''Given two integers left and right, return the count of numbers 
in the inclusive range [left, right] having a prime number of set bits 
in their binary representation. Recall that the number of set bits an integer 
has is the number of 1's present when written in binary. 
For example, 21 written in binary is 10101, which has 3 set bits.
 

Example 1:

Input: left = 6, right = 10
Output: 4
Explanation:
6  -> 110 (2 set bits, 2 is prime)
7  -> 111 (3 set bits, 3 is prime)
8  -> 1000 (1 set bit, 1 is not prime)
9  -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.'''


def countPrimeSetBits(left: int, right: int) -> int:
    cnt = 0
    for i in range(left, right + 1):
        a = count_ones(i)
        b = prime(a)
        if b:
            cnt += 1
    return cnt


import  math

def prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_ones(n):
    cnt = 0
    while n:
        if n & 1:
            cnt += 1
        n >>= 1
    return cnt

'''You have a set of integers s, which originally contains all the 
numbers from 1 to n. Unfortunately, due to some error, one of the 
numbers in s got duplicated to another number in the set, which results 
in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of 
this set after the error.
Find the number that occurs twice and the number that is 
missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]'''


def findErrorNums(nums):
    twice = sum(nums) - sum(set(nums))
    res = 1
    nums.sort()
    flag = False
    nums.remove(twice)

    if nums[0] != 1:
        return [twice, 1]
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] != 1:
            res = nums[i - 1] + 1
            flag = True
            break
    if flag:
        return [twice, res]
    return [twice, nums[len(nums) - 1] + 1]