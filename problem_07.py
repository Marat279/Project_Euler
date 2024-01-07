def print_hi(source):
    it = 1
    score = 1
    while score < source:
        it += 2
        a = 0
        for i in range(1, it, 2):
            if it % i == 0:
                a += 1
                if a == 2:
                    break
        if a == 1:
            score += 1
    print(it)


if __name__ == '__main__':
    print_hi(10001)
