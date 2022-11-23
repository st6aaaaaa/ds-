'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?'''


def climbStairs(n) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    arr = [None] * (n)
    arr[0] = 1
    arr[1] = 2
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n - 1]