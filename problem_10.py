def print_hi(source):
    result = 2
    for i in range(3, source, 2):
        a = 0
        print(i)
        for j in range(3, int(i/3)+1, 2):
            if i % j == 0:
                a += 1
                if a != 0:
                    break
        if a == 0:
            result += i
    print(result)


if __name__ == '__main__':
    print_hi(2000000)
