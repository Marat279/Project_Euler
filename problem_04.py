def print_hi(source):
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            a = i * j
            b = str(a)
            if b == ''.join(reversed(b)):
                print(b)
                break


if __name__ == '__main__':
    print_hi(3)
