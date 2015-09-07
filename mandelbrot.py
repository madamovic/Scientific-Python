import numpy as np
import matplotlib.pyplot as pl
from numpy import newaxis

def compute_mandelbrot(N_max,some_threshold,nx,ny):
	x=np.linspace(-2,1,nx)
	y=np.linspace(-1.5,1.5,ny)
	c=x[:,newaxis]+1j*y[newaxis,:]
	z=c
	for j in xrange(N_max):
		z=z**2+c
		mandelbrot_set=(abs(z)<some_threshold)
		return mandelbrot_set

mandelbrot_set=compute_mandelbrot(50,50.,601,401)
pl.imshow(mandelbrot_set.T,extent=[-2.1,2.1,-1.5,1.5])
pl.gray()
pl.savefig('mandelbrot.png')
