def isBoolean():
    return True


def checkIsTrue(a, b):
    return a == b


if __name__ == '__main__':
    print(isBoolean())
    print(checkIsTrue(6, 7))
    print(checkIsTrue(6, 6))
    print(checkIsTrue("6", "7"))
    print(checkIsTrue("6", "6"))
    print(True is True)
    print(True is False)



