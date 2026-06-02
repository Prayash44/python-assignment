r = int(input("Rows: "))
c = int(input("Columns: "))

a = []
b = []
s = []

print("Enter first matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    a.append(row)

print("Enter second matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    b.append(row)

for i in range(r):
    row = []
    for j in range(c):
        row.append(a[i][j] + b[i][j])
    s.append(row)

print("Sum Matrix:")
for row in s:
    print(row)