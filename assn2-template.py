import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1


def recbinsearch(L, l, u, target):
    idx = -1
    while (l <= u):
        mid = int((l+u)/2)
        if L[mid] == target :
            idx = mid
            break
        elif L[mid] < target :
            l = mid + 1
        else :
            u = mid - 1
    return idx

def binsearch(nbrs, target):
    lower = 0
    upper = len(nbrs) - 1
    idx = -1
    while (lower <= upper):
        middle = int((lower + upper) // 2)
        if nbrs[middle] == target :
            idx = middle
            break
        elif nbrs[middle] < target :
            lower = middle + 1
        else:
            upper = middle - 1
    return idx



numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# binary search
cnt = 0
for target in targets:
    idx = binsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("Binary Search %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()