#Check whether a bit is a set(1) or not
def setOrNot(number, n):

    if number & (1 << (n - 1)):
        print("SET")
    else:
        print("NOT SET")

number = int(input("Enter the number: "))
n = int(input("Enter the bit position: "))
setOrNot(number, n)

'''
#Write a Program to check the rightmost set bit in your number n = 42 #101010
count = 1
while True:
    if n & 1 == 1:
        break
    else:
        count += 1

    n = n>>1
print(count)
''' 