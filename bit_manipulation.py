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


