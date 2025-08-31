print("1. Read entire file:")
file = open("sample.txt", "r")
content = file.read()
print(content)

# 2. Read file line by line using a loop
print("\n2. Read line by line using a loop:")
file = open("sample.txt", "r")
for line in file:
    print(line.strip())  

print("\n3. Read one line at a time using readline():")
file = open("sample.txt", "r")
line1 = file.readline()
line2 = file.readline()
print("Line 1:", line1.strip())
print("Line 2:", line2.strip())

print("\n4. Read all lines into a list using readlines():")
file = open("sample.txt", "r")
lines = file.readlines()
print(lines)