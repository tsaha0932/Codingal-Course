#algorithm for finding all prime numbers up to any given limit
def SieveOfEratosthenes(num): #6
    prime = [True for i in range(0, num + 1)]
    #prime = [True, True, True, True, True, True, True]
    p = 2
    while ( p * p <= num): #4<6, 9<6

        if (prime[p] == True):

            for i in range( p * p, num + 1, p): #range(4,7,2) ---> i = 4,6
                prime[i] = False #prime = [True, True, True, True, False, True, False]
            p += 1 #p = 3
    
    for p in range(2, num + 1):#range(2,7) ---> i = 2,3,4,5,6
        if prime[p] == True:
            print(p, end = ", ")#2,3,5

num = int(input("Enter an integer"))
print("Following are the prime numbers smaller")
print("than or equal to", num)
SieveOfEratosthenes(num)