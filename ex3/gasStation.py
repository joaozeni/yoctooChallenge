def gasStation(strArr):
    index, start = 1, 1
    remaining_sum, total = 0, 0
    for gas_station in strArr:
        gasAmount, gasNeeded = gas_station.split(":")
        remaining = int(gasAmount) - int(gasNeeded)
        if remaining_sum >= 0:
            remaining_sum += remaining
        else:
            remaining_sum = remaining
            start = index

        total += remaining
        index += 1

    if total >= 0:
        return start
    else:
        return "impossible"


if __name__ == "__main__":
    tests = open('tests', 'r')
    lines = tests.readlines()

    for line in lines:
        obj = eval(line)[1:]
        result = gasStation(obj)
        print(result)
        print('-------------------------')
