#Program to find HCF/GCD

#Enter 2 numbers

numberLargest = int(input("Enter Largest number : "))#12
numberSmallest = int(input("Enter Smallest number : "))#10

#using Euclidean Algorithm
while(numberSmallest): #10>0, 2>0
    numberStore = numberSmallest #10, 2
    numberSmallest = numberLargest % numberSmallest #2, 0
    numberLargest = numberStore #10,2

print(f"HCF of {numberLargest} and {numberSmallest} is : ", numberLargest)