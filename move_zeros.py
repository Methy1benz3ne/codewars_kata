# def move_zeros(array):
#     count = 0
#     for i in array:
#         if i == 0.0 or 0 :
#             array.pop(count)
#             array.append(0)
#             # count -= 1
#         count += 1
#     return array



def move_zeros(array):
    i = 0
    for m in array :
        if m != 0 or m is False:
            i +=1
    for m in range(i):
        if array[m] is not False :
            array = pop1(array,m)

    return array

def pop1(array,i):
    if array[i] == 0 :
        array.pop(i)
        array.append(0)
        if array[i] == 0:
            pop1(array,i)
    return array

print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))