def sum_pairs(ints,s):
    i =0
    li = []
    jmin = 0
    while i < len(ints):
        j=i+1
        while j < len(ints):
            if ints[i] + ints[j] == s:
                    # li.append([i,j])
                    if jmin is 0 or j < jmin :
                        jmin = j
                        li = [i,j]
            j += 1
        i += 1
    # m=0
    # mini= 0
    if li == []:
        return None
    else:
        # for aa in li :
        #     if aa[1] == jmin :
        res = [ints[li[0]],ints[li[1]]]

        # res = [ints[li[mini][0]], ints[li[mini][1]]]
        return res

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
print(sum_pairs(l4, 2))