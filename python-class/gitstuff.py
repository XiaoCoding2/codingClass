def is_p(x):
    x = str(x)
    list = []
    for y in range(0, len(x)):
        a = x[y] == x[-(y+1)]
        list.append(a)
    if False in list:
        return False
    return True
print(is_p(1000021))