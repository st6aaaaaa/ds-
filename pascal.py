'''Given an integer rowIndex, return the rowIndexth (0-indexed)
row of the Pascal's triangle. In Pascal's triangle, each number
is the sum of the two numbers directly above it as shown:'''

# first recursive  solution

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


# second dynamic solution

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

### other_solution_pascal_r(3) -> [1,3,3,1]
