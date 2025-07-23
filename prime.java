public class prime {

    public static void main(String[] args) {
        System.out.println("Prime numbers from 1 to 100 are:");

        // Outer loop to iterate through numbers from 1 to 100
        for (int i = 1; i <= 100; i++) {
            // Check if the current number 'i' is prime
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
    }

    // Function to check if a number is prime
    public static boolean isPrime(int num) {
        // 0 and 1 are not prime numbers
        if (num <= 1) {
            return false;
        }
        // Check for divisibility from 2 up to the square root of num
        // We only need to check up to the square root because if a number 'num' has a divisor greater than its square root,
        // it must also have a divisor smaller than its square root.
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false; // Not a prime number if divisible by 'i'
            }
        }
        return true; // Is a prime number if no divisors found
    }
}