#take input values from user
x = input("Enter value of x:")
y = input("Enter value of y:")


#Swapping
temp = x #temp = 23, x= 23, y= 78
x = y #temp = 23, x= 78, y= 78
y = temp #temp= 23, x= 78, y= 23

#Single line swap
#x,y = y,x

#Displaying results after swapping
print("value of x after swapping", x)
print("value of y after swapping", y)