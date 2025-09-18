import time
def OnTime(n):
    iteration=0
    for i in range(1, n+1):
        iteration+=1
    print("When n is ",n,"Iterations = ",iteration)

OnTime(10)
OnTime(20)
OnTime(42)

print("\n With every 'n' the time taken and iteration will increase")

start = time.time()
OnTime(1000)
end = time.time()
print(f"Function took : {end - start:.10f} seconds")