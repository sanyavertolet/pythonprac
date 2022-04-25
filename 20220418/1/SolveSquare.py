
def solveSquare(a, b, c):
	"""Find root of equation ax^2 + bx + c = 0."""
	d = b * b - 4 * a * c
	if d < 0:
		return None
	elif d == 0:
		root = -b / (2 * a)
		return (root, root)
	else:
		sqrt_d = d ** (1/2)
		return ((-b - sqrt_d) / (2 * a), (-b + sqrt_d) / (2 * a))