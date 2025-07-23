import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    """
    if num < 0:
        return False
    
    original_num = num
    sum_of_factorials = 0
    
    # Calculate factorial for digits 0-9 to optimize
    factorials = [math.factorial(i) for i in range(10)]

    while num > 0:
        digit = num % 10
        sum_of_factorials += factorials[digit]
        num //= 10
    
    return sum_of_factorials == original_num

def find_strong_numbers_in_range(start, end):
    """
    Finds and prints all strong numbers within a specified range.
    """
    print(f"Strong numbers between {start} and {end}:")
    found_strong_numbers = []
    for i in range(start, end + 1):
        if is_strong_number(i):
            found_strong_numbers.append(i)
    
    if found_strong_numbers:
        for strong_num in found_strong_numbers:
            print(strong_num)
    else:
        print("No strong numbers found in this range.")

# Find strong numbers from 1 to 5000
find_strong_numbers_in_range(1, 5000)