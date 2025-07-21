
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = [1,2,3,4,5,6,7,8]
y = [1,2,3,4,5,6,7,8]

def error(w,b,x,y):
    e=0
    for val in range(0,len(x)):
        e+=(w*x[val]+b-y[val])**2
    return e

x_vals=[]
y_vals=[]
z_vals=[]
for w in range(1,1001):
    for b in range(1,1001):
        w_s=w/10
        b_s=b/10
        x_vals.append(w_s)
        y_vals.append(b_s)
        e=error(w_s,b_s,x,y)
        z_vals.append(e)
# define your data
#convert lists to arrays so you can reshape
x_arr = np.array(x_vals)
y_arr = np.array(y_vals)
z_arr = np.array(z_vals)

# rebuild the grid
X, Y = np.meshgrid(np.unique(x_arr), np.unique(y_arr))

# now reshape your flat z array into the proper matrix
Z = z_arr.reshape(len(np.unique(y_arr)), len(np.unique(x_arr)))

# plot the surface with color
fig = plt.figure(figsize=(10,7))
ax  = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(
    X, Y, Z,
    cmap='viridis',
    edgecolor='k',
    linewidth=0.3
)

fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Error')

ax.set_xlabel('m (slope)')
ax.set_ylabel('b (intercept)')
ax.set_zlabel('Error')
ax.set_title('Error Surface over (m,b)')

plt.show()