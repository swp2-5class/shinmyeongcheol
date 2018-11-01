import time
list = [0,1]
def Iterfibo(x):
    for i in range(2,x+1):
        if i >= 2 :
            result = list[i-2] + list[i-1]
            list.append(result)
    a = list[x]
    return a

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)
while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    start = time.time()
    fibonumber2 = Iterfibo(nbr)
    end = time.time() - start
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
    print("IterFibo({})={}  time {}".format(nbr,fibonumber2,end))