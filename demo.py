def compare(a, b):
    ret = 0
    if a > b:
        ret = a
    else:
        ret = b
    return ret


print(compare(3, 8))
print(compare(5, 6))
print(compare(10, 2))
