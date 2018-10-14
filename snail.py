def snail(array):
    if not array:
        return array
    res = list()
    n = len(array)
    res += array.pop(0)
    for i in range(n-2):
        res.append(array[i].pop())
    if array:
        res += array.pop()[::-1]
    for i in range(n-2,0,-1):
        res.append(array[i-1].pop(0))
    res += snail(array)
    return res
