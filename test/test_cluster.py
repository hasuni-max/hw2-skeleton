from hw2skeleton import cluster
from hw2skeleton import io, find_features, kmeans, hier, scoring
import os



def test_partition_clustering():
    # tractable subset
    pdb_ids = [276, 4629, 10701]

    active_sites = []
    for id in pdb_ids:
        filepath = os.path.join("data", "%i.pdb"%id)
        active_sites.append(io.read_active_site(filepath))

    features = find_features.calc_features(active_sites)
    
    data = []
    for res,feature_vect in features.items():
        data.append(kmeans.data_point(label=res,data=tuple(feature_vect)))

    km = kmeans.kmeans(data=data,k=3,threshold=3)
    km.cluster()
    # update this assertion
    assert len(km.centroids.items()) >= 1


def test_hierarchical_clustering():
    # tractable subset
    pdb_ids = [276, 4629, 10701]

    active_sites = []
    for id in pdb_ids:
        filepath = os.path.join("data", "%i.pdb"%id)
        active_sites.append(io.read_active_site(filepath))
    
    features = find_features.calc_features(active_sites)

    for res,feature_vect in features.items():
        hier.hierarchical("V" + res, feature_vect, metric='Euclidian')

    assert hier.hierarchical.Cluster()
