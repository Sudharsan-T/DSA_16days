def count_even(numbers, version = 1):
    if version == 1:
        result = 0
        for x in numbers:
            if x % 2 == 0:
                result += 1
        return result
    elif version == 2:
        return sum(1 for x in numbers if x % 2 == 0)

#max_diff
def max_diff(numbers, version = 1):
    if version == 1:
        result = 0
        for x in numbers:
            for y in numbers:
                result = max(result, abs(x - y))
        return result
    elif version == 2:
        numbers = sorted(numbers)
        return numbers[-1] - numbers[0]
    elif version == 3:
        return max(numbers) - min(numbers) #efficient way
    
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result