def merge_sort(a):
    if len(a) <= 1 :
        return a

    pivot = int(len(a)/2)
    left = merge_sort(a[0:pivot])
    right = merge_sort(a[pivot:])
    return merge(left,right)

def merge(a,b):
    ret = []
    left_cursor = right_cursor = 0

    while left_cursor < len(a) and right_cursor<len(b):
        if a[left_cursor] < b[right_cursor]:
            ret.append(a[left_cursor])
            left_cursor+=1
        else:
            ret.append(b[right_cursor])
            right_cursor+=1
    ret.extend(a[left_cursor:])
    ret.extend(b[right_cursor:])
    return ret

a= [5,4,3,2,1,0,-1]
a = merge_sort(a)
print(a)