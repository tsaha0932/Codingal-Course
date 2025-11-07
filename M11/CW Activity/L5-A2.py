#Write a program to divide 2 numbers without using division operator
def divide(ourdividend, ourDivisor):
    sign = (-1 if((ourdividend < 0) ^ (ourDivisor < 0)) else 1)
    ourdividend = abs(ourdividend)
    ourDivisor = abs(ourDivisor)

    quotientNumber = 0
    tempNumber = 0

    for i in range(31, -1, -1):
        if(tempNumber + (ourDivisor << i) <= ourdividend): #0+(3*2**2) <= 13
            tempNumber += ourDivisor << i # 0+(3<<2) = 3*2**2 = 12
            quotientNumber |= 1 << i #0 or 1<<2 = 000 or 100 = 100 = 4
    
    if sign == -1:
        quotientNumber = -quotientNumber
    return quotientNumber


a = int(input("Enter a for a/b: ")) #dividend
b = int(input("Enter b for a/b: ")) #divisor
print("Result of", a, "/", b, "is", divide(a, b))

#a = 13 = 1101
#b = 3 = 0011

#3<<1 = 110 = 3*2**1
#11<<2 = 1100 = 3*2**2