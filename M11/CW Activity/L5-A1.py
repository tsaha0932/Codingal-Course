#Swapping 2 numbers
def swap(a,b): #a=2=10, b=3=11 
    a = a^b #10 ^ 11 = 01
    b = a^b #01 ^ 11 = 10 = 2
    a = a^b #01 ^ 10 = 11 = 3
    print("After swapping: a=",a,"and b =",b)

def swap2(a,b):
    a = (a&b)+(a|b) # (10 & 11 = 10) + (10 | 11 = 11) = 10+11 = 101 = 5
    b = a+(~b)+1 # a + (-b-1) +1 = a-b = 5-3 = 2
    a = a+(~b)+1 #a-b = 5-2 = 3
    print("After swapping: a=",a,"and b =",b)

swap(10,20)
swap2(10,20)



#~b = -b-1
#-b = ~b+1
#2 = 0000 0000
#~2 = 1111 1111
#~2+1 = 1111 1101 + 0000 0001 = 1111 1110 = -2
#01+01 = 10