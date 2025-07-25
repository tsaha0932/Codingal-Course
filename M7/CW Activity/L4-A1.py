num = int(input("Enter the number: "))
print(f"Table of {num}")
for i in range(1,11):
      mul = num*i
      print("%d x %d = %d" % (num,i, mul))