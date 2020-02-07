from hw2skeleton import cluster
from hw2skeleton import io, find_features, kmeans, hier, scoring
import os

def test_similarity():
    #sign(dist(a,b))==+
    pdb_ids = [276, 4629]

    active_sites = []
    for id in pdb_ids:
        filepath = os.path.join("data", "%i.pdb"%id)
        active_sites.append(io.read_active_site(filepath))
    
    features = find_features.calc_features(active_sites)
    assert scoring.L2(features['276'],features['4629']) > 0


def test_distance_to_self():
    #dist(a,a)==0
    pdb_ids = [276]

    active_sites = []
    for id in pdb_ids:
        filepath = os.path.join("data", "%i.pdb"%id)
        active_sites.append(io.read_active_site(filepath))
    
    features = find_features.calc_features(active_sites)
    x = scoring.L2(features['276'],features['276'])

    assert x == 0.0

def test_recip_distance():
    #dist(a,b)==dist(b,a)
    pdb_ids = [276,4629]

    active_sites = []
    for id in pdb_ids:
        filepath = os.path.join("data", "%i.pdb"%id)
        active_sites.append(io.read_active_site(filepath))
    
    features = find_features.calc_features(active_sites)

    assert scoring.L2(features['276'],features['4629']) == scoring.L2(features['4629'],features['276'])



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
    assert len(km.centroids.items()) == 3


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
