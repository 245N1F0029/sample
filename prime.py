def is_prime(num):
    """
    Checks if a given number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True  # If no divisors found, it's prime

def find_primes_in_range(start, end):
    """
    Finds and prints all prime numbers within a specified range (inclusive).
    """
    print(f"Prime numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=" ")
    print() # For a new line after printing all primes

# Call the function to find primes from 1 to 100
find_primes_in_range(1, 100)