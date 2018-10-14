def tribonacci(signature, n):
    result = []

        result.append(signature[0])
        result.append(signature[1])
        result.append(signature[2])
        for i in range(n - 3):
            result.append(result[i] + result[i + 1] + result[i + 2])
    return result
