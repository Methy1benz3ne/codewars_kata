def find_it(seq):
    seq.sort()
    i=0
    count=0
    # return seq
    while i < len(seq):
        count = 0
        j=0
        while j < len(seq):
            if seq[i]== seq[j] :
                count += 1
            j+=1
        if count%2 ==1 :
            return seq[i]
    # return seq
        i +=1

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))