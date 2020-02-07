

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

def calc_features(active_sites):
	features = {}
	for act in active_sites:
		features[act.name] = []

		number_of_residues = len(act.residues)
		three_letter = [str(x)[0:3] for x in act.residues]
		plus_charge, minus_charge = find_charge(three_letter)
		number_of_chains = len(act.chains)

		features[act.name].append(number_of_residues) #number of residues
		features[act.name].append(plus_charge) #number of plus charges - done
		features[act.name].append(minus_charge) #number of minus charges - done
		features[act.name].append(number_of_chains) #number of chains - done

	return features

