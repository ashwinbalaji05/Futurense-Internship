def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)

def main():
    num = int(input("Enter a number: "))

    if is_prime(num):
        print("The number is prime.")
        print("Sum of its digits:", sum_of_digits(num))
    else:
        print("The number is not prime.")
        print("Factorial of the number:", factorial(num))

if __name__ == "__main__":
    main()
