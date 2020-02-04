import math
import random
import numpy as np
import matplotlib.pyplot as plt


class data_point():

	label_counter = 0
	all_points = []
	def __init__(self,label="",data=tuple()):
		self.label = label
		self.data = data

		if self.label == "":
			self.label = str(data_point.label_counter)
			data_point.label_counter += 1


class kmeans(object):
	"""
		Kmeans object that takes data (list of data_point objects) and contains 
		a clustering method that clusters data using k centroids and a specified 
		distance metric
	"""
	def __init__(self,data,k,threshold=5,distance_metric="euclid"):
		self.data = data #list of of data_point objects
		self.k = k #number of centroids
		self.centroids = None #This will eventually become a dictionary when clustering() is called
		self.threshold = threshold #Param for number of times to update centroids

		if distance_metric == "euclid":
			self.distance_metric = self.euclidean_distance
		else:
			pass #add other distance metrics
		

	def cluster(self):
		"""
			Main method that performs kmeans clustering
		"""

		update = 0
		self.update_centroids() #set centroids 
		while update < self.threshold: 
			temp_centroids = {}
			for point in self.data: #for each data point calculate...
				best = 99999
				assigned_key = None
				for cent in self.centroids.keys(): #..its distance to the current centroids
					dist = self.distance_metric(point.data,cent)
					if dist < best: #keep track of what 
						
						assigned_key = cent
						best = dist

				if assigned_key not in temp_centroids.keys():
					temp_centroids[assigned_key] = []
					temp_centroids[assigned_key].append(point)
				else:
					temp_centroids[assigned_key].append(point)
				
				#self.centroids[assigned_key].append(point)
			self.centroids = temp_centroids
			self.update_centroids()
			update += 1

	def update_centroids(self):
		"""
			For each centroid, create a new vector that is centered around data
			in its respective cluster. Update self.centroids
		"""

		if not self.centroids:
			self.centroids = {pt.data:[] for pt in random.sample(self.data, self.k)}

		else:
			temp = {}

			for k,v in self.centroids.items(): #k = [features] v = [data_point objects]
				updated_vec = self.average_vector(v)

				temp[updated_vec] = v

			self.centroids = temp

	def euclidean_distance(self,vec1,vec2):
		"""
			Takes two tuples and calculates the euclidean distance between them
		"""
		summed = sum([(x-y)**2 for x,y in zip(vec1,vec2)])
		return math.sqrt(summed)

	def average_vector(self,point_objects):
		"""
			Input: list of data_point objects

			Given a list of data_point objects, take the average of every dimension
			and store it to a new vector. 
			
			Returns: A tuple with updated averaged weights

		"""
		out_vector = []
		for item in point_objects:
			"""
				For each data vector add each of its indices to a out_vector
			"""
			for i, val in enumerate(item.data):
				try:
					out_vector[i] += val
				except:
					out_vector = out_vector + [val]

		out_vector = [x/len(point_objects) for x in out_vector]
		#print(tuple(out_vector))
		return tuple(out_vector)

	def __str__(self):
		pass

def generate_random_arrays(n):
	"""
		Generates a list of length n with random integers between 1 and 1000 using 
		the sample function in the random module
	"""

	l = [random.randrange(1, 3) for _ in range(0, n)]

	return l

def intra_distance(cluster):

	pass
	
def inter_distance():
	pass

def silhouette_score(cluster1,cluster2):
	a = intra_distance(cluster1)
	b = intra_distance(cluster1,cluster2)
	pass


if __name__ == "__main__":

	points = []
	for x in range(5):
		set1 = np.random.normal(5, 2, 2)
		set2 = np.random.normal(20, 2, 2)
		points.append(tuple(set1))
		points.append(tuple(set2))

	print(len(points))

	data = []
	for point in points:
		data.append(data_point(data=point))

	#print(len(data))
	ha = kmeans(data=data,k=2)
	ha.cluster()
	#print(ha.centroids.values())

	cents = []
	for centroid, points in ha.centroids.items():
		print(centroid,len(points))
		cents.append(points)

	# print(ha.data)

	# silhouette_score(points[0],points[1])
	# cluster = 1
	# for k,v in ha.centroids.items():
	# 	temp = []
	# 	for val in v:
	# 		temp.append(val.data)
		
	# 	x, y = temp[0], temp[1]

	# 	plt.plot(x,y,label=str(cluster))
	# 	cluster += 1

	# plt.legend()
	# plt.xlabel("X")
	# plt.ylabel("Y")
	# plt.show()
	



