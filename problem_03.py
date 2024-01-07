def print_hi(source):
    a = 0
    for i in range(1, int(source ** 0.5)):
        if source % i == 0:
            for j in range(3, i, 2):
                if i % j == 0:
                    a += 1
            if a == 0:
                b = i
                print(b)


if __name__ == '__main__':
    print_hi(600851475143)