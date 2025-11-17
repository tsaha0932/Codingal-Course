def longest_consecutive_ones(n):
    binary = bin(n)[2:]
    max_count = 0
    current_count = 0

    for bit in binary:
        if bit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

num = int(input("Enter a number: "))
print("Longest consecutive 1s:", longest_consecutive_ones(num))