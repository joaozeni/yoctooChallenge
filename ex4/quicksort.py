def partition(arr, low, high):
    smaller_index = (low - 1)
    pivot_value = arr[high]

    for index in range(low, high):
        if arr[index] <= pivot_value:
            smaller_index += 1
            arr[smaller_index],arr[index] = arr[index],arr[smaller_index]

    arr[smaller_index+1],arr[high] = arr[high],arr[smaller_index+1]

    return smaller_index+1


def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)


if __name__ == "__main__":
    tests = open('tests', 'r')
    lines = tests.readlines()

    for line in lines:
        obj = eval(line)
        result = quicksort(obj)
        print(obj)
        print('-------------------------')
