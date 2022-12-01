'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as sho

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]'''


def generate(numRows: int) :
    arr = [[1] * i for i in range(1, numRows + 1)]
    for i in range(2, numRows):
        for j in range(1, i):
            arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]
    return arr