def check_the_methode_of_len():
    # len() the methode to check the length of a variable or input and array list
    result = len("hello")
    result2 = len("test")

    print(result)
    print(result2)

    result3 = len([0, 1, 2, 3, 4])
    print(result3)
    result4 = ["test", "test2"]


def check_the_methode_of_str():
    # Convert an integer variable to a string
    print(str(6))
    print(str("6"))


def check_the_methode_of_sorted():
    variable = [7, 1, 2, 3, 4, 5, 6]
    result = sorted(variable)
    print(result)

    variable2 = ["x", "V", "N ", "X ", "T", "B", "n"]
    result = sorted(variable2)
    print(result)


if __name__ == '__main__':
    greeting = "Hello World"
    word = greeting.split(" ")[0]
    print("Hello" == word)

    # Check the length of the input
    # check_the_methode_of_len()

    # Check if the input convert to string
    # check_the_methode_of_str()

    # Check and sort the array
    check_the_methode_of_sorted()
