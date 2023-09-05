import numpy as np
import timeit
import math, random

def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    
    # Calculate how many digits there are, then divide that by 2
    # note: this is faster than calculating len(str()) and comparing
    # n = max(len(str(x)), len(str(y)))
    # note: this doesn't account for negative values of x or y
    if x == 0:
        n = math.floor(math.log10(y)) + 1
    elif y == 0:
        n = math.floor(math.log10(x)) + 1
    else:
        n = max((math.floor(math.log10(x)) + 1), (math.floor(math.log10(y)) + 1))
    n = n // 2
    
    # Get the left half of X and Y by using (number // 10^n)
    # Then get the right half by using (number % 10^n)
    a = x // (10 ** n)
    b = x % (10 ** n)
    c = y // (10 ** n)
    d = y % (10 ** n)
    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a+b), (c+d)) - ac - bd

    # Divided n by 2 earlier, so we have to multiply n in the original
    # formula by 2.
    # og formula: (10^n)(ac) + (10^(n/2))(ad+bc) + bd
    return(((10**(n*2)) * ac) + ((10**(n)) * ad_bc) + bd)

if __name__ == "__main__":
    # testcase
    # for i in range(100):
    #     x = random.randint(1, 2**1024)
    #     y = random.randint(1, 2**1024)
    #     assert(karatsuba(x, y) == x * y)
    # else:
    #     print('OK')

    # Actual question   
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    # x = 1234
    # y = 5678
    assert(karatsuba(x, y) == x * y)
    print(karatsuba(x, y))