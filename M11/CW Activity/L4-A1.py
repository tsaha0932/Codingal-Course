#Write a program to check if a number is power of 2
def power2(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0

n = int(input("Enter a number: "))
if power2(n):
    print("\nThe number is a power of 2")
else:
    print("\nThe number is not a power of 2")

#10 & 01
#100 & 011
#1000 & 0111
#10000 & 01111