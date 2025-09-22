def sum(n):
    return n*(n+1/2)

#Space complexity:0(1), Auxiliay space=0(1)
#Linear space:
def arraysum(a):
    sum=0
    for i in a:
        sum = sum + i

    return sum

a = [12,3,4,15]
arraysum(a)

#With the size of the array, the space also required increases.
#Space complexity:0(n), Auxiliary space=0(1)
def summ(n):
    if (n<=0):
        return
    return n+ summ(n-1)