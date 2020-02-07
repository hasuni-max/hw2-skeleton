import sys
import matplotlib.pyplot as plt
import numpy as np
from .io import read_active_sites, write_clustering, write_mult_clusterings
from .find_features import find_charge
from .kmeans import kmeans, data_point
from .hier import hierarchical
from .scoring import silhouette_score

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


if sys.argv[1] == "-P":
	print("Running kmeans")
	data = []
	for res,feature_vect in features.items():
		data.append(data_point(label=res,data=tuple(feature_vect)))

	km = kmeans(data=data,k=3,threshold=20)
	km.cluster()

	clusts = []
	for k,v in km.centroids.items():
		clusts.append([i.data for i in v])

	s = silhouette_score(*clusts)
	print("Average silhouette_score for kmeans", sum(s)/len(s))

elif sys.argv[1] == "-H":
	print("Running hierarchical")

	for res,feature_vect in features.items():
		hierarchical("V" + res, feature_vect, metric='Euclidian')

	hierarchical.Cluster()


	clust1 = hierarchical.all_data["V10701"]
	clust2_names = []
	clust2_data = []
	clust3_names = []
	clust3_data = []
	hierarchical.DFS(hierarchical.nodes["NODE129"],clust2_names,clust2_data)
	hierarchical.DFS(hierarchical.nodes["NODE132"],clust3_names,clust3_data)
	# print(clust3_data)
	print(clust1)
	print(clust2_data)
	s = silhouette_score([clust1],clust2_data,clust3_data)

	print("Average silhouette_score for hierarchical", sum(s)/len(s))



else:
	print("Please specify clustering type")




