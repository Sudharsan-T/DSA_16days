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

#Time complexity
#Constant Time - no loops[O(1)]:
def middle(numbers):
    n =len(numbers)
    return numbers[n // 2]

#Single loop [O(n)]:
def calc_sum(numbers):
    result = 0
    for x in numbers:
        result += x
    return result

#Nested Loops [O(n^2)]
def has_sum(number, x):
    for a in numbers:
        for b in numbers:
            if a + b == x:
                return True
    return False
#If algorithm has 'K' nested loops each of which goes through all elements of the input [O(n^k)]

#Sequential Code Segments
def count_min(numbers):
    #stage-1
    min_value = numbers[0]
    for x in numbers:
        if x < min_value:
            min_value = x
    #stage-2
    result = 0
    for x in numbers:
        if x == min_value:
            result += 1

    return result

'''
Stage 1's TC is O(n)
Stage 2's TC is also O(n)
So combined TC will also be O(n)
'''