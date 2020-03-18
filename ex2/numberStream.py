def numberStream(input_str):
    current_value = None
    count_value = 0

    for value in input_str:
        if value != current_value:
            count_value = 1
            current_value = value
        else:
            count_value += 1

        if int(value) == count_value:
            return True

    return False


if __name__ == "__main__":
    tests = open('tests', 'r')
    lines = tests.readlines()

    for line in lines:
        obj = eval(line)
        result = numberStream(obj)
        print(result)
        print('-------------------------')
