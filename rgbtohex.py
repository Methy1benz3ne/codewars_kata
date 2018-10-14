def rgb(r,g,b):
    if r > 256 :
        r1 = 'FF'
    elif r<0 :
        r1 = '00'
    else:
        r1 = str(hex(r))[2:]
        if len(r1) == 1:
            r1 = '0' + r1

    if g > 256:
        g1 = 'FF'
    elif g <0:
        g1 = '00'
    else:
        g1 = str(hex(g))[2:]
        if len(g1) == 1:
            g1 = '0' + g1

    if b > 256:
        b1 = 'FF'
    elif b <0 :
        b1 = '00'
    else:
        b1 = str(hex(b))[2:]
        if len(b1) == 1:
            b1 = '0' + b1

    res = r1 + g1 + b1
    res = res.upper()
    return res

print(rgb(0,0,0))