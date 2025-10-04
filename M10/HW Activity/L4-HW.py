def binary_to_decimal():
    while True:
        binary_str = input("Enter your Binary (or type 'exit' to quit): ")
        
        if binary_str.lower() == 'exit':
            print("Exiting program.")
            break
        
        # Validate if input is a binary number
        if all(bit in '01' for bit in binary_str):
            decimal = int(binary_str, 2)
            print("Decimal:", decimal)
        else:
            print("Invalid binary number. Please enter only 0s and 1s.")

# Run the converter
binary_to_decimal()