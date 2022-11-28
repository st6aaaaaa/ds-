'''Given an integer array nums, return true if any
value appears at least twice in the array,
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
def finc(nums):
     import collections as col
     c = col.Counter(nums)

     return True if c.most_common(1)[0][1] > 1 else False

a =finc([1,1,1,3,3,4,3,2,4,2])
print(a)