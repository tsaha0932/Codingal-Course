import time

def fun1(n):
    return n*(n+1)/2

def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(i, i+1):
            sum += 1
    return sum

n = 1000

start = time.time()
fun1(n)
end = time.time()
print(f"Function took : {end - start:.10f} seconds")

start = time.time()
fun2(n)
end = time.time()
print(f"Function took : {end - start:.10f} seconds")

start = time.time()
fun3(n)
end = time.time()
print(f"Function took : {end - start:.10f} seconds")