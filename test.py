a = [[1,2],[3,4]]
b = [[a[i][j] for i in range(2)] for j in range(2)]


a[1][1:2] = [3]

print(a)

print(b)