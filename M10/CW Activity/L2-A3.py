import time
def ONSquareTime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            #print("*", end =" ")
            iteration+=1
        print("")
    print("\n When n is ",n," Iterations = ",iteration, "\n")

ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)

print("\n With every 'n' the time taken equals n^2")
print("O(n^2)")

start = time.time()
ONSquareTime(1000)
end = time.time()
print(f"Function took : {end - start:.10f} seconds")