myLanguages = list()


def setList(language):
    myLanguages.append(language);


def getList():
    return myLanguages


if __name__ == '__main__':
    print([0, 0, 0][1])
    print(["Python", "Java", "C#"][2])
    setList("NL")
    setList("BE")
    print(getList())
