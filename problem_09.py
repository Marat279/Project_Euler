def print_hi(source):
    for i in range(1, 998):
        for j in range(i, 999):
            for k in range(j, 1000):
                if i ** 2 + j ** 2 == k ** 2 and i + j + k == 1000:
                    print(i * j * k)
                    break


if __name__ == '__main__':
    print_hi(1000)
