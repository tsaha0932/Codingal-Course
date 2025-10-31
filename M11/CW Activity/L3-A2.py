#Finding which number from the array appears odd number of times.
#Assumption: Only one number appear odd number of times

def OddOccuring(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []
n = int(input("Enter array size: "))
while(n):
    num = int(input("Enter number: "))
    arr.append(num)
    n-=1
print("Odd occuring number is",OddOccuring(arr))

'''
[6,3,5,6,3]
[110, 011, 101, 110, 011]
[110 ^ 000 = 110, 011 ^ 110 = 101, 101 ^ 101 = 000, 110 ^ 000 = 110, 011 ^ 110 = 101 = 5]
'''