import sys
from .io import read_active_sites, write_clustering, write_mult_clusterings
from .cluster import cluster_by_partitioning, cluster_hierarchically
from .find_features import find_charge
# read_active_sites("../data")



# Some quick stuff to make sure the program is called correctly
if len(sys.argv) < 4:
    print("Usage: python -m hw2skeleton [-P| -H] <pdb directory> <output file>")
    sys.exit(0)

active_sites = read_active_sites(sys.argv[2])


features = {}
#number of residues
#number of plus charges - done
#number of minus charges - done
#number of chains 
for act in active_sites:
	features[act.name] = []

	three_letter = [str(x)[0:3] for x in act.residues]
	plus_charge, minus_charge = find_charge(three_letter)
	number_of_chains = len(act.chains)

	features[act.name].append(plus_charge)
	features[act.name].append(minus_charge)
	features[act.name].append(number_of_chains)

print(features)

# # Choose clustering algorithm
# if sys.argv[1][0:2] == '-P':
#     print("Clustering using Partitioning method")
#     clustering = cluster_by_partitioning(active_sites)
#     write_clustering(sys.argv[3], clustering)

# if sys.argv[1][0:2] == '-H':
#     print("Clustering using hierarchical method")
#     clusterings = cluster_hierarchically(active_sites)
#     write_mult_clusterings(sys.argv[3], clusterings)
