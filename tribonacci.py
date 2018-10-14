def tribonacci(signature, n):
    result=[]
    if n < 3 :
        for i in range(n):
            result.append(signature[i])

    else:
        result.append(signature[0])
        result.append(signature[1])
        result.append(signature[2])
        for i in range(n-3):
            result.append(result[i]+result[i+1]+result[i+2])
    return result

# Test.describe("Basic tests")
print(tribonacci([1, 1, 1], 10))
# .assert_equals(tribonacci([0.5, 0.5, 0.5], 30), [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5])