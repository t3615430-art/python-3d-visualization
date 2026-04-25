import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(15, 10))

# 1. Волна
ax1 = fig.add_subplot(221, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax1.plot_surface(X, Y, Z, cmap='plasma')
ax1.set_title('Хвиля')

# 2. Спіраль
ax2 = fig.add_subplot(222, projection='3d')
t = np.linspace(0, 10*np.pi, 1000)
ax2.plot(np.sin(t), np.cos(t), t/10, color='cyan', linewidth=2)
ax2.set_title('Спіраль')

# 3. Гори
ax3 = fig.add_subplot(223, projection='3d')
X2 = np.random.uniform(-5, 5, (50, 50))
Y2 = np.random.uniform(-5, 5, (50, 50))
Z2 = np.sin(X2) * np.cos(Y2)
ax3.plot_surface(X2, Y2, Z2, cmap='terrain')
ax3.set_title('Гори')

# 4. Сфера
ax4 = fig.add_subplot(224, projection='3d')
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax4.plot_surface(x, y, z, cmap='coolwarm')
ax4.set_title('Сфера')

plt.tight_layout()
plt.show()
