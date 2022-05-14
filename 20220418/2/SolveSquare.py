from SquareIO import SquareIO

def solveSquare(a, b, c):
	"""Find root of equation ax^2 + bx + c = 0."""
	if a == 0:
		if b == 0:
			if c == 0:
				return True
			else:
				return None
		else:
			return -c / b
	else:
		d = b * b - 4 * a * c
		if d < 0:
			return None
		elif d == 0:
			root = -b / (2 * a)
			return (root, root)
		else:
			sqrt_d = d ** (1/2)
			return ((-b - sqrt_d) / (2 * a), (-b + sqrt_d) / (2 * a))
