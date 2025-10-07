n = int(input("Enter the number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print(f"Fibonacci sequence up to {n} terms:")
    print(a, b, end=' ')
    for _ in range(2, n):
        next_term = a + b
        print(next_term, end=' ')
        a, b = b, next_term
