def get_rightmost_set_bit_position(n):
    if n == 0:
        return 0 
    position = 1
    while (n & 1) == 0:
        n >>= 1  
        position += 1  
    return position
number1 = 18   
number2 = 12 
number3 = 7   
number4 = 0  

print(f"The rightmost set bit for {number1} is at position: {get_rightmost_set_bit_position(number1)}")
print(f"The rightmost set bit for {number2} is at position: {get_rightmost_set_bit_position(number2)}")
print(f"The rightmost set bit for {number3} is at position: {get_rightmost_set_bit_position(number3)}")
print(f"The rightmost set bit for {number4} is at position: {get_rightmost_set_bit_position(number4)}")