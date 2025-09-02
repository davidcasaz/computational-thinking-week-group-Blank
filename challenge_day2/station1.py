# station1.py

def solution_station_1(n: int) -> int:
    # Return the n-th Fibonacci number
    # Fibonacci sequence: F1 = 1, F2 = 1, F3 = 2, ...
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    if n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
