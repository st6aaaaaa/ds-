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

arr = [1024,512,256,128,64,32,16,8,4,2,1]
arr = quicksort(arr)
print(arr)


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