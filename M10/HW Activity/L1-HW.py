def multiply_one_iteration(a, b):
    return a * b

def multiply_n_iterations(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result if b >= 0 else -result

a = 5
b = 6

result_one = multiply_one_iteration(a, b)
result_n = multiply_n_iterations(a, b)

print("1 iteration:", result_one)
print("N iteration:", result_n)
