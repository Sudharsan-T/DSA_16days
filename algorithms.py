def count_even(numbers, version = 1):
    if version == 1:
        result = 0
        for x in numbers:
            if x % 2 == 0:
                result += 1
        return result
    elif version == 2:
        return sum(1 for x in numbers if x % 2 == 0)

