def fibonacci(n):
    """
    Compute the nth Fibonacci number efficiently using an iterative approach.
    
    This implementation has O(n) time complexity and O(1) space complexity,
    making it more efficient than the naive recursive approach.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    if n <= 1:
        return n
    
    # Use iterative approach for efficiency
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


def fibonacci_optimized(n):
    """
    Compute the nth Fibonacci number using the most efficient method.
    
    This uses matrix exponentiation with O(log n) time complexity.
    Based on the identity: [[1,1],[1,0]]^n = [[F(n+1),F(n)],[F(n),F(n-1)]]
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    if n <= 1:
        return n
    
    def matrix_multiply(A, B):
        """Multiply two 2x2 matrices."""
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]
    
    def matrix_power(matrix, power):
        """Compute matrix^power using iterative binary exponentiation for efficiency."""
        result = [[1, 0], [0, 1]]  # Start with the identity matrix
        
        while power > 0:
            # If power is odd, multiply the current result by the matrix
            if power % 2 == 1:
                result = matrix_multiply(result, matrix)
            
            # Now, square the matrix and halve the power
            matrix = matrix_multiply(matrix, matrix)
            power //= 2
            
        return result
    
    # Base matrix [[1,1],[1,0]]
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n)
    
    return result_matrix[0][1]


def fibonacci_sequence(n):
    """
    Generate the first n Fibonacci numbers.
    
    Args:
        n (int): The number of Fibonacci numbers to generate
    
    Returns:
        list: A list containing the first n Fibonacci numbers
    
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    if n == 0:
        return []
    
    sequence = [0]
    if n == 1:
        return sequence
    
    sequence.append(1)
    
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence


if __name__ == "__main__":
    # Test the functions
    print("Testing Fibonacci functions:")
    
    # Test basic cases
    test_values = [0, 1, 2, 5, 10, 15, 20]
    
    for n in test_values:
        fib_iterative = fibonacci(n)
        fib_matrix = fibonacci_optimized(n)
        print(f"n={n}: iterative={fib_iterative}, matrix={fib_matrix}")
        assert fib_iterative == fib_matrix

    print("\nTesting sequence generation:")
    for n in [0, 1, 10]:
        print(f"Sequence for n={n}: {fibonacci_sequence(n)}")

    print("\nTesting error handling:")
    try:
        fibonacci(-1)
    except ValueError as e:
        print(f"Caught expected error for negative input: {e}")

    try:
        fibonacci(1.5)
    except TypeError as e:
        print(f"Caught expected error for non-integer input: {e}")

    print("\nAll tests completed.")
