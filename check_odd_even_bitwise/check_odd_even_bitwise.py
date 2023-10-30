def check_odd_even(n) -> str:
    return "odd" if n & 1 else "even"


if __name__ == '__main__':
    test = check_odd_even(21)
    print(test)
