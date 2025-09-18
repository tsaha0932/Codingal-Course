import time
#Program to show Constant Time Complexity

def printnumber(n):
    iteration=0
    print("The number entered by the user is ",n)
    iteration+=1
    print("Total iterations done by the code is ",iteration,"\n")

printnumber(10)
printnumber(20)
print("\n With any 'n' the time taken by our code won't change")

start = time.time()
printnumber(1000)
end = time.time()
print(f"Function took : {end - start:.10f} seconds")