def fibonacci(n):
    if n in [0, 1]:
        return n
    me = [0,1]
    fi=[0,1]
    if n not in [0,1]:
        if n in me:
            return fi[n]
        else :
            for i in range(2,n+1) :
                fi.append(fi[i-1]+fi[i-2])
                me.append(i)
            return fi[n]

# for i in range(2,3):
print(fibonacci(11))


#
# def memory(n):
#     if n in me:
#      return fi(n)
#
#     if n < max1:
#
#     me[n] = fibonacci(n-1)+fibonacci(n-2)
#

