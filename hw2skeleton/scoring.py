
from math import sqrt


def L2(x_vector,y_vector):
    deltas = sum([(x_vector[i] - y_vector[i])**2 for i in range(len(x_vector))])
    return sqrt(deltas)

def intra_distance(point,cluster):
	"""
		Within group distances
	"""
	distance = 0 
	for val in cluster:
		if point == val:
			pass
		else:
			distance += L2(point,val)
	
	if len(cluster) == 1:
		return distance
	else: 
		return distance/(len(cluster)-1) #substract one for when point == val
	# print(point,cluster)
	
def inter_distance(point,*args):
	"""
		Returns the minimum inter distance
	"""
	dists = []
	for clust in args:
		distance = 0
		for val in clust:
			distance += L2(point,val)

		if len(clust) == 1:
			dists.append(distance)
		else:
			dists.append(distance/len(clust))

		
	return min(dists)

def silhouette_score(*args):
	"""
		Input: Two lists (clusters) that contain data point (lists)
		Output: A list containing silhouette scores for each data doint

	"""
	outlist = []
	for cluster in args:
		temp = list(args)
		temp.remove(cluster) #these are all other clusters used for inter calculations

		for point in cluster:
			if len(cluster) == 1:
				a = 0.00000001
			else:
				a = intra_distance(point,cluster)
			b = inter_distance(point,*temp)
			denom = max(a,b)
			s = (b-a)/denom
			outlist.append(s)
	return outlist


if __name__ == "__main__":
	x = [[1,2,4],[3,5,6],[6,8,9],[3,2,1]]
	y = [[6,2,4],[0,5,2],[6,2,9]]
	z = [[3,2,4],[3,5,7],[1,8,9],[3,8,1]]
	h = [[3,2,4],[3,5,7],[1,8,9],[3,8,1]]
	p = [[1,1,1],[5,5,6],[0,8,1],[3,0,1]]


	silhouette_score(x,y)


