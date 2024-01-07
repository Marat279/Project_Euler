def print_hi(source):
    a = 0
    b = 1
    c = 0
    d = 0
    while c < source:
        c = a + b
        a = b
        b = c
        if c % 2 == 0:
            d = d + c
    print(d)


if __name__ == '__main__':
    print_hi(4000000)
