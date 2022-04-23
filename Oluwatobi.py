- 👋 Hi, I’m @Oluwatobi-makee
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Oluwatobi-makee/Oluwatobi-makee is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
---
import numpy as np
import matplotlib.pyplot as plt

DX = int(input("Enter values for DX: "))
DY = int(input("Enter values for DY: "))
X1old= int(input("Enter values for X1old: "))
Y1old = int(input("Enter values for Y1old: "))
X2old = int(input("Enter values for X2old: "))
Y2old = int(input("Enter values for Y2old: "))
X3old = int(input("Enter values for X3old: "))
Y3old = int(input("Enter values for Y3old: "))

X1new = DX + X1old
Y1new = DY + Y1old

X2new = DX + X2old
Y2new = DY + Y2old

X3new = DX + X3old
Y3new = DY + Y3old
print("X1new =", X1new)
print("X2new =", X2new)
print("Y1new =", Y1new)
print("Y2new =", Y2new)

A = [X1old,X2old,X3old]
B = [Y1old,Y2old,Y3old]
C = [X1new,X2new,X3new]
D = [Y1new,Y2new,Y3new]

plt.scatter(A, B, label='Xold and Yold', color='b')
plt.scatter(C, D, label='Xnew and Ynew', color='g')
plt.xlabel('X*axis')
plt.ylabel('Y*axis')
plt.title('2D Translation')
plt.legend()
plt.show()

