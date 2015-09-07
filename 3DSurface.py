import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
fig=pl.figure()
ax=Axes3D(fig)
x=np.arange(-4,4,0.25)
y=np.arange(-4,4,0.25)
x,y=np.meshgrid(x,y)
R=np.sqrt(x**2+y**2)
z=np.sin(R)
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap=pl.cm.hot)
ax.contourf(x,y,z,zdir='z',offset=-2,cmap=pl.cm.hot)
ax.set_zlim(-2,2)
pl.show()
