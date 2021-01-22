import math
def fast_square(z,n):
    if (z/3) < 10**(n/2) or n is 1:
        return z**2
    else:
        return fast_square(z/3, n) + (2*fast_square(2*z/3,n))


z=72211000
n = int(math.log10(z/3)+1)
print(z**2)
print(fast_square(z, n))

def fast_square_2(z,n):
    if (z/6) < 10**(n/3) or n is 1:
        return z**2
    else:
        return fast_square(z/6, n) + (2*fast_square(2*z/6,n)) + (3*fast_square_2(3*z/6,n))


z=5999000
n = int(math.log10(z/3)+1)
print(z**2)
print(fast_square_2(z, n))