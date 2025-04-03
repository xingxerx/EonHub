def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n: The non-negative integer.

    Returns:
        The factorial of n.
        Raises ValueError if n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")  # Output: The factorial of 5 is 120
