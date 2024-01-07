def print_hi(source):
    b = 0
    a = 2520
    c = 0
    while b == 0:
        for i in range(1, source+1):
            if a % i == 0:
                c += 1
                if c == 20:
                    b += 1
                    print(a)
                    break
            if a % i != 0:
                c = 0
                break
        a += 10


if __name__ == '__main__':
    print_hi(20)
