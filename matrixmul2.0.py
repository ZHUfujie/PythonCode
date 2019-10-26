#计算矩阵乘积，目前只能计算正矩阵
#!/usr/bin/env python3
n1 = int(input("Enter the row value of matrix A: "))
m1 = int(input("Enter the column value of matrix A: "))
print("Enter values for the Matrix A")
a = []
for i in range(n1):
    a.append([int(x) for x in input().split()])
n2 = int(input("Enter the row value of matrix B: "))
m2 = int(input("Enter the column value of matrix B: "))
print("Enter values for the Matrix B")
b = []
for i in range(n2):
    b.append([int(x) for x in input().split()])
c = []
d = []
for i in range(n1):
    for j in range(m2):
        d.append(a[i][j] * b[j][i])
    print(d)
    c.append(d)
    d = []
    #c.append([a[i][j] * b[j][i] for j in range(m2)])
print("After matrix multiplication")
print("-" * 7 * m1)
print(c)
#for x in c:
    #print(x)
    #for y in x:
        #print(str(y).rjust(5), end=' ')
    #print()
#print("-" * 7 * m1)
