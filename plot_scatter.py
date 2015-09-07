import numpy as np
import pylab as pl
n=1024
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
t=np.arctan2(y,x)
pl.axes([0.025,0.025,0.95,0.95])
pl.scatter(x,y,s=75,c=t,alpha=.5)
pl.xlim(-1.5,1.5)
pl.xticks(())
pl.ylim(-1.5,1.5)
pl.yticks(())
pl.show()
