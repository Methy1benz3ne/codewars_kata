def sum_pairs(ints,s):
    i=len(ints)
    li=[]
    while i > 0 :
        j= i-1
        while j > 0:
            if ints[i-1] + ints[j-1]== s:
                li.append([i,j])
                # break
            j -= 1
        # if li != []:
        #     break
        i -= 1

    if li == [] :
        return None
    else :
        return [ints[li[0][]],ints[li[1]]]

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
print(sum_pairs(l4, 2))