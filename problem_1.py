def print_hi(source):
    a = 0
    for i in range(source):
        if i % 5 == 0 or i % 3 == 0:
            a = a + i
    print(a)


if __name__ == '__main__':
    print_hi(1000)
