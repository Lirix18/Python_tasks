def odd_nums(number):
    for num in range(1, number + 1, 2):
        yield num


if __name__ == '__main__':
    odd_to_15 = odd_nums(15)
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
