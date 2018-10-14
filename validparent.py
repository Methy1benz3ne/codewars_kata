def valid_parentheses(string):
    res = 0
    for ch in string :
        if ch == ')' :
            res-=1
        if ch == '(' :
            res += 1
        if res <0 :
            return False
    if res == 0:
        return True
    else : return False