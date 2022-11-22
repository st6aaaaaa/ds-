
def palindrome(s):
    if len(s)<=1:
        return s
    return s[-1] + palindrome(s[:-1])

def pal1(s,start,end):
    if start>=end:
        return
    s[start],s[end] = s[end],s[start]
    pal1(s,start+1,end-1)

from collections import defaultdict

def findTheDistanceValue( arr1, arr2, r: int) -> int:
    d = defaultdict(list)
    for a1 in arr1:
        for a2 in arr2:
            d[a1].append(abs(a1 - a2))
    cnt = 0
    print(d)
    for k in arr1:
        if all(e > r for e in d[k]):
            cnt += 1
    return cnt

def pascal(i,j):
    if  j==0:
        return 1
    if i == j :
        return 1
    return pascal(i-1,j) + pascal(i-1,j-1)

def rowPascal(row):
    a= []
    if row % 2 == 1 :
        for i in range((row+1)//2):
            tmp = pascal(row,i)
            a.append(tmp)
        b = list(reversed(a))

    else :
       for i in range(row//2 + 1):
           tmp = pascal(row,i)
           a.append(tmp)
       b = list(reversed(a[:len(a)-1]))
    a.extend(b)
    print(a)

def other_solution_pascal_r(row):
    if row == 0 :
        return [1]
    if row == 1 :
        return [1,1]


    arr_2d = [ [None for j in range(row+1) ] for i in range(row+1)]

    for i in range(row+1):
        arr_2d[i][0] = 1
        arr_2d[i][i] = 1

    for i in range(2,row+1):
        for j in range(1,i):
            arr_2d[i][j] = arr_2d[i-1][j] + arr_2d[i-1][j-1]
    print(arr_2d[row])


other_solution_pascal_r(3)

