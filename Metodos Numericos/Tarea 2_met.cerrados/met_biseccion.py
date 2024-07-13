def f(x):
	return -25+82*x-90*x**2+44*x**3-8*x**4+0.7*x**5

def Met_biseccion(f,xl,xu,es,imax):
	iter = 0
	
	ea = 0


	while(ea < es or iter >= imax):
		xrold = xr
		xr = (xl + xu) / 2
		iter = iter + 1
		if(xr != 0):
			ea = abs((xr - xrold) / xr) * 100

		test = f(xl) * f(xr)
		if(test < 0):	
		    xu = xr
		elif(test > 0):
		    xl = xr
		else:
		    ea = 0

	Met_biseccion = xr

	print(xr)

Met_biseccion(f,0.5,1,0.0002,100)
