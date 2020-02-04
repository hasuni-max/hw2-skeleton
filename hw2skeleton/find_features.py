

global plus
global minus

minus = ["ASP","GLU"]
plus = ["ARG","HIS","LYS"]

def find_charge(residues):
	"""
		Takes a list of residues and returns the number of plus and 
		minus charged residues.

		This function uses the global plus and minus variables
	"""
	global plus
	global minus

	plus_charge = sum([res in plus for res in residues])
	minus_charge = sum([res in minus for res in residues])

	return plus_charge, minus_charge


