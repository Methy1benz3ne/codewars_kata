def move_zeros(array):
    for m in array :
        if type(m) is not bool:
            if m ==0 or m ==0.0:
                if type(m) ==int or type(m) == float :
                    array.remove(m)
                    array.append(0)
    return array

print(move_zeros([1,1,1,1,23,22,0,0,0,0,0,False,1]))