#Program to find if a number is Armstrong number

#take input from the user
number = int(input("Input your number: "))

#Calculate number of digits
digits = len(str(number))

#Initialize result variable
resultNumber = 0

#find the sum of the a^digits of each digit
temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //= 10

#display the result
if number == resultNumber:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")