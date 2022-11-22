'''Write a function that takes an unsigned integer and returns the number of '1'
bits it has (also known as the Hamming weight)'''


# first solution :)
def hammingWeight( n) :
    return list(bin(n)[2:]).count('1')


# second_solution
def sec_sol(n):
    cnt = 0
    while n > 0:
        if n%2 == 1 :
            cnt+=1
        n //= 2
    return cnt


# third solution
def third_sol(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (1 if n % 2 == 1 else 0) + third_sol(n // 2)

def fouth_sol(n):
    m = 1
    bits = 0
    for i in range(32):
        if n & m != 0 :
            bits+=1
        m = m<<1


    print(bits)

fouth_sol(63)


