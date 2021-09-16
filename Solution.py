import numpy

n = int(input().split(" ")[0])

A = []
for y in range(n):
    row = input().split(" ")
    for x in range(n):
        row[x] = int(row[x])      
    A.append(row)
B = []
for y in range(n):
    row = input().split(" ")
    for x in range(n):
        row[x] = int(row[x])      
    B.append(row)


print(numpy.matmul(A,B))
