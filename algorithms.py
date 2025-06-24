def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even2(numbers):
    return sum(1 for x in numbers if x % 2 == 0)

print(count_even([1, 9, 4]))         
print(count_even([9, 2, 5, 12, 72]))  
print(count_even([5, 4, 1, 7, 9, 6])) 
print(count_even2([1, 2, 3]))         
print(count_even2([2, 2, 2, 2, 2]))   
print(count_even2([5, 4, 1, 7, 9, 6]))