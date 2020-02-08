import math
cosp = 1/math.sqrt(2)
cosy = math.sqrt(3)/2
siny = 1/2
a = [[cosp,0,-cosp],[0,1,0],[cosp,0,cosp]]
b = [[cosp,0,-cosp],[0,1,0],[cosp,0,cosp]]
c = [[cosp,0,-cosp],[0,1,0],[cosp,0,cosp]]
print(a[0],sep='\n')
print(a[1],sep='\n')
print(a[2],sep='\n')
print(sep='\n')
summ = (a[0][0] * a[1][1] * a[2][2]) - (a[0][0] * a[1][2]*a[2][1]) - (a[0][1]*a[1][0]*a[2][2])+(a[0][1]*a[1][2]*a[2][0])+(a[0][2]*a[1][0]*a[2][1])-(a[0][2]*a[1][1]*a[2][0])
summ = 1/summ
print(summ)
print(sep='\n')
b[0][0] = a[1][1]*a[2][2] - a[1][2]*a[2][1]
b[0][1] = a[0][2]*a[2][1] - a[0][1]*a[2][2]
b[0][2] = a[0][1]*a[1][2] - a[0][2]*a[1][1]
b[1][0] = a[1][2]*a[2][0] - a[1][0]*a[2][2]
b[1][1] = a[0][0]*a[2][2] - a[0][2]*a[2][0]
b[1][2] = a[0][2]*a[1][0] - a[0][0]*a[1][2]
b[2][0] = a[1][0]*a[2][1] - a[1][1]*a[2][0]
b[2][1] = a[0][1]*a[2][0] - a[0][0]*a[2][1]
b[2][2] = a[0][0]*a[1][1] - a[0][1]*a[1][0]
print(b[0],sep='\n')
print(b[1],sep='\n')
print(b[2],sep='\n')
print(sep='\n')
for x in range(0,3):
    for y in range(0,3):
        c[x][y] = a[x][0]*b[0][y] + a[x][1]*b[1][y] + a[x][2]*b[2][y]
        if c[x][y] > 0.9999:
            c[x][y] = 1

print(c[0],sep='\n')
print(c[1],sep='\n')
print(c[2],sep='\n')
