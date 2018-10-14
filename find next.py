def find_next_square(sq):
    if pow(sq,0.5).is_integer() is False :
        return -1
    else :
        a1 = pow(sq, 0.5)
        a1 += 1
        ans = pow(a1, 2)

        return ans
