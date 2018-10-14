import math
def iter_pi(epsilon):
    res = 1
    i=0
    pi1 = 0.
    while res >= epsilon :
        pi1 += pow(-1,i) / (2*(i+1) - 1)
        res = abs(4*pi1-math.pi)
        i+=1
        # print(pi1)
        b = '%.10f' %(4*pi1)
    return [i, float(b)]

print(iter_pi(0.1))