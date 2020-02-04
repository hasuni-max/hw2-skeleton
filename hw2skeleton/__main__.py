import sys
import matplotlib.pyplot as plt
import numpy as np
# import hierarchical as hier
from .io import read_active_sites, write_clustering, write_mult_clusterings
from .cluster import cluster_by_partitioning, cluster_hierarchically
from .find_features import find_charge
from .kmeans import kmeans, data_point
from .hier import hierarchical

# Some quick stuff to make sure the program is called correctly
if len(sys.argv) < 4:
    print("Usage: python -m hw2skeleton [-P| -H] <pdb directory> <output file>")
    sys.exit(0)

active_sites = read_active_sites(sys.argv[2])


# Grab various features 
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


## Run clusterings
data = []
for res,feature_vect in features.items():
	data.append(data_point(label=res,data=tuple(feature_vect)))
	hierarchical("V" + res, feature_vect, metric='Euclidian')

# ha = kmeans(data=data,k=3,threshold=20)
# ha.cluster()

# for k,v in ha.centroids.items():
# 	print(k,len(v))

hierarchical.Cluster()



# xs = []
# ys = []
# hierarchical.DFS(hierarchical.nodes["NODE134"],xs,ys)
# print(xs)
# print(ys)


xs = []
ys = []
hierarchical.DFS(hierarchical.nodes["NODE3"],xs,ys)
print(len(xs))
# print(len(ys))

xs = []
ys = []
hierarchical.DFS(hierarchical.nodes["NODE133"],xs,ys)
print(len(xs))
# print(len(ys))


# # Choose clustering algorithm
# if sys.argv[1][0:2] == '-P':
#     print("Clustering using Partitioning method")
#     clustering = cluster_by_partitioning(active_sites)
#     write_clustering(sys.argv[3], clustering)

# if sys.argv[1][0:2] == '-H':
#     print("Clustering using hierarchical method")
#     clusterings = cluster_hierarchically(active_sites)
#     write_mult_clusterings(sys.argv[3], clusterings)
