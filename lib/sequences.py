#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    fibonacci = [0, 1] if length > 1 else [0]

    for i in range(2, length):
        next_number = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_number)

    print(fibonacci)