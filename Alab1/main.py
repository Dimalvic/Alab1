from collections import deque
from timeit import default_timer as timer



def merge(a, lo, mi, hi):
    aux_lo = deque(a[lo:mi])
    aux_hi = deque(a[mi:hi])

    for i in range(lo, hi):
        if aux_lo and aux_hi:
            a[i] = aux_lo.popleft() if aux_lo[0] < aux_hi[0] else aux_hi.popleft()
        elif aux_lo:
            a[i] = aux_lo.popleft()
        elif aux_hi:
            a[i] = aux_hi.popleft()

def find_next_stop(a, start):
    upper = len(a) - 1
    if start >= upper:
        return start

    stop = start + 1
    if a[start] <= a[stop]:
        while stop < upper and a[stop] <= a[stop+1]:
            stop += 1
    else:
        while stop < upper and a[stop] >= a[stop+1]:
            stop += 1

        end = stop
        while start < end:
            a[end], a[start] = a[start], a[end]
            start += 1
            end -= 1
    return stop

def natural_merge(a):
    upper = len(a) - 1
    if upper <= 0:
        return
    while True:
        mi = find_next_stop(a, 0)
        if mi == upper:
            return
        hi = find_next_stop(a, mi)
        merge(a, 0, mi, hi)




file1GB = input("Enter file name: ")
file1 = open(file1GB)
newList = []
for line in file1:
    line = line.rstrip()
    numbers = line.split()
    for number in numbers:
        newList.append(number)
file1.close()

file2GB = input("Enter file name: ")
file2 = open(file2GB)

newList1 = []
for line in file2:
    line = line.rstrip()
    numbers = line.split()
    for number in numbers:
        newList1.append(number)
file2.close()


start = timer()
natural_merge(newList)
end = timer()
print( end - start,  ' Seconds')
start1 = timer()
natural_merge(newList1)
end1 = timer()
print( end1 - start1, ' Seconds')



