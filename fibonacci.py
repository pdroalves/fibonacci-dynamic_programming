def fib_standard(n):
	if n < 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

def fib_dynamic_programming_aux(n,F):
	if n < 2:
		return 1
	else:
		if not F[n-1]:
			F[n-1] = fib_dynamic_programming_aux(n-1,F)
		if not F[n-2]:
			F[n-2] = fib_dynamic_programming_aux(n-2,F)
		return F[n-1]+F[n-2]

def fib_dynamic_programming(n):
	F = [None for x in range(n)]
	return fib_dynamic_programming_aux(n,F)
