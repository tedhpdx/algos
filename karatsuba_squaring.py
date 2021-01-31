


import math



def fast_square(n,m):
    if n < 10**(m/2) or m is 1:
        return n**2
    else:
        return fast_square(n/3, m) + (2*fast_square(2*n/3,m))


z=72211000
n = int(math.log10(z/3)+1)
print(z**2)
#print(fast_square(z, n))

def fast_square_2(n,m):
    if (n/6) < 10**(m/3) or m is 1:
        return n**2
    else:
        return fast_square_2(n/6, m) + (2*fast_square_2(2*n/6,m)) + (3*fast_square_2(3*n/6,m))


z=5999000
n = int(math.log10(z/3)+1)
print(z**2)
print(fast_square_2(z, n))

