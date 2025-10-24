#Check the count of zeroes and one bits in the number we have entered
def numberOfBits(n):
    ones = 0
    zeroes = 0
    while(n):
        if (n & 1 == 1):
            ones += 1
        else:
            zeroes += 1
        n = n >> 1
    print("Number of ones = ", ones, "\nNumber of zeroes = ", zeroes)

number = int(input("Enter your number: "))
numberOfBits(number)

#AND, OR, NOT, XOR, <<, >>
#5 AND 9= 0101 & 1001 = 0001 = 1
#5 OR 9 = 0101 | 1001 = 1101 = 13
#5XOR 9 = 0101 ^ 1001 = 1100 = 12
#5<<n = 101<<n = 5*2**(n)
#5>>n = 101 >> n = 5//2**(n)