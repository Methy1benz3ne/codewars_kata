def add(input):
    if input is None:
        return 0
    return input + add()


print(add(1)(2)(3))