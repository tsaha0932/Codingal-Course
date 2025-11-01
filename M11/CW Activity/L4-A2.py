#Check if a number is power of 4
def powerOf4(number):
    #Check if a number is positive and is a power of 2
    if number <= 0 or (number & (number - 1)) !=0:
        return False

    count = 0
    while number > 1:
        number >>= 1
        count += 1

    #Check if the only set bit is at an even position
    return count % 2 == 0

number = int(input("Enter your number : "))
if(powerOf4(number)):
    print(number, 'is a power of 4')
else:
    print(number, 'is not a power of 4')

#1 & 1 = 1 - power of 4
#10 & 11 = 10 - not power of 4
#100 & 111 = 100 - power of 4
#1000 & 1111 = 1000 - not power of 4
#10000 & 11111 = 10000 - power of 4