def reverse_bits(n):
    reversed_num = 0
    for i in range(32):
        if (n >> i) & 1:
            reversed_num |= (1 << (31 - i))
    return reversed_num

if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        reversed_bits_num = reverse_bits(num)
        print(f"The number with bits reversed is: {reversed_bits_num}")
    except ValueError:
        print("Invalid input. Please enter an integer.")