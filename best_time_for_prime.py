#####################################################################
#                  Python program for Prime number                  #
#                                                                   #
#####################################################################


import math
import time

# Using sqrt
def prin_till_N1(x):
    for num in range(2, x + 1):
        for i in range(2, int(math.sqrt(num))+1):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")

# Using //2
def prin_till_N2(x):
    for num in range(2, x + 1):
        for i in range(2, num//2+1):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")

# Normal Iteration
def prin_till_N3(x):
    for num in range(2, x + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")

if __name__ == "__main__":
    n = int(input())
    a= time.time()
    prin_till_N1(n)
    print(time.time()-a)
    b=time.time()
    prin_till_N2(n)
    print(time.time()-b)
    c=time.time()
    prin_till_N3(n)
    print(time.time()-c)
