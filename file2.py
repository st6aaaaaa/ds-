
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


#other_solution_pascal_r(3)

a =2.500006103515625
import math
#print(math.ceil(a), math.floor(a)+0.5)
#b = (math.floor(a) if a < math.floor(a)+0.5
 #               else  math.ceil(a) )
#print(b)

from binarytree import build

def depth_tree(node):
    if node is None :
        return 0

    left_d = depth_tree(node.left)
    right_d = depth_tree(node.right)
    return max(left_d, right_d) + 1


def d_tree(node):
    stack = []
    dep = 0
    if node is not None:
        stack.append((1,node))

    while stack != [] :
        cur_d , n = stack.pop()
        if n is not None :
            dep = max(dep, cur_d)
            stack.append((cur_d  + 1 , n.left))
            stack.append((cur_d + 1 , n.right))

    return dep



def rev(n):
    if n=='1':
        return '0'
    if n=='0':
        return '1'
    return rev(n[:len(n)//2]) + rev(n[len(n)//2:])

def gram(n):
    if n==1:
        return '0'
    if n == 2 :
        return '01'
    arr = [None] * n
    arr[0] = '0'
    arr[1] = '01'
    for i in range(2,n):
        arr[i] = arr[i-1] + rev(arr[i-1])
    return arr[n-1]

def kthGrammar(n,k):
    a = gram(n)
    return a[k-1]

def f2(n):
    if n==1:
        return '0'
    if n==2:
        return '01'
    arr = [None] * n
    arr[0] = '0'
    arr[1] = '01'
    for i in range(2,n):
        arr[i] = arr[i-1] + arr[i-1][len(arr[i-1])//2:] + arr[i-1][:len(arr[i-1])//2]

    return arr[n-1]


def func3(n):
    if n==1 :
        return '0'
    if n==2:
        return '1'
    arr = [None]* n
    arr[0] = '0'
    arr[1] = '01'
    for i in range(2,n):
        arr[i] = arr[i-1]
        for j in arr[i-1][len(arr[i-1])//2:]:
            if j==0:
                arr[i]+='01'
            else :
                arr[i]+='10'
    print(arr)

def func4(n,k):
    k = k-1
    if n==1 :
        return 0
    if n==2 and k==0:
        return 0
    if n==2 and k==1:
        return 1

    if k%2 == 1 :
        return  (func4(n-1,(k-1)/2) + 1 ) % 2
    else :
        return (func4(n-1,k/2) + 1 ) % 2


def from_bin_to_dec(a):

            res = 0
            power = 0
            a = int(a)
            while a > 0:
                rem = a % 10
                res = res + rem*2**power
                power+=1
                a //=10

            return res

def from_dec_to_bin(a):
    # a '100'



from_bin_to_dec('11')