def isValidWalk(walk):
    x = 0
    y = 0
    if len(walk) < 10:
        return False
    for a in walk:
        if a == 'n' :
            y += 1
        if a == 's' :
            y -= 1
        if a == 'e' :
            x += 1
        if a == 'w' :
            x -= 1
    if x==0 and y==0:
        return True
    else :
        return False
