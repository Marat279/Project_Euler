def print_hi(source):
    a = 0
    b = 0
    for i in range(101):
        a = i ** 2 + a
        b = i + b
    print(b ** 2 - a)


if __name__ == '__main__':
    print_hi(100)
