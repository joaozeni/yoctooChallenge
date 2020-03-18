def scaleBalancing(strArr):
    balance_weights = eval(strArr[0])
    weight1, weight2 = balance_weights[0], balance_weights[1]
    difference = abs(weight1 - weight2)
    extra_weights = eval(strArr[1])
    set_extra_weights, set_needed_weights = set(), set()
    for weight in extra_weights:
        needed_weight = abs(difference - weight)
        if needed_weight == 0:
            return weight
        if weight in set_needed_weights:
            return [weight, needed_weight]
        if needed_weight in set_extra_weights:
            return [weight, needed_weight]

        set_needed_weights.add(needed_weight)
        set_extra_weights.add(weight)
    
    return None


if __name__ == "__main__":
    tests = open('tests', 'r')
    lines = tests.readlines()

    for line in lines:
        obj = eval(line)
        result = scaleBalancing(obj)
        print(result)
        print('-------------------------')
