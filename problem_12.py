import math


def print_hi(source):
    result = 0
    triag = 0
    nature = 0
    while result < source:
        nature += 1
        result = 0
        triag += nature
        for i in range(1, int(math.sqrt(triag + 1))):
            if triag % i == 0:
                result += 1
        result *= 2
    print(triag)


if __name__ == '__main__':
    table = 500
    print_hi(table)
