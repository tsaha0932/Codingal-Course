s = input("Enter string: ")
n = len(s)

for length in range(1, n+1):
    for i in range(n - length + 1):
        print(s[i : i + length])