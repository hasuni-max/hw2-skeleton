import random
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt



class hierarchical(object):

    nodes = {} #Dictionary that contains the entire tree structure (parent-child relationships)       
    distance = {} #Keeps track of distances calculated. Keys: A tuple with internal names. Val: Distance
    #Reverse keys are also stored

    #Below are a set of global variables that are used to keep track of best distanes
    #while constructing tree
    dummy = -1000
    bestDistance = nextBestDistance = -1000
    bestLeft = str
    bestRight = str
    nextLeft = str
    nextRight = str

    metric = str
    linkage = str

    def __init__(self, name, data, metric='Euclidian', right=None,
                 left=None, represented=None, linkage = "Single" ):

        self.name = name #file name
        self.right = right #leafs will be set to None 
        self.left = left #leafs will be set to None
        self.taken = False
        self.data = data

        # a list with elements corresponding to names/keys of all child nodes of this node instance
        if not represented:
            self.represented = [name]
        else:
            self.represented = represented


        if metric == 'Euclidian': #assign distance_function to the desired method and from there distance_function will stay that.
            self.distance_function = self.L2
            hierarchical.metric = 'Euclidian'
        elif metric == "Single": #Note that if you want to change linkage you must change hierarchical.metric in clustering
            self.distance_function = self.single
            hierarchical.metric = 'Single'
        elif metric == "Complete":
            self.distance_function = self.complete


        # print("Instantiating node " + self.name)

        # The new instance now calculates the distance between itself and other non-paired instances
        # this could be implemented as a separate private method rather than directly within the constructor
        other_list = []
        for next_node in hierarchical.nodes.values(): #memory address
            
            if next_node.taken is False:  # Check to make sure that we are dealing with an unpaired node
                other_list.append(next_node.name)
                 #if data is a list
                node_pair = (self.name, next_node.name)
                #print "BROOO LOOK AT THIS LINE", node_pair
                hierarchical.distance[node_pair] = self.distance_function(next_node)
                #here is where we will modify it

                hierarchical.distance[next_node.name, self.name] = hierarchical.distance[node_pair]


                if hierarchical.distance[node_pair] > hierarchical.bestDistance:

                        hierarchical.bestDistance = hierarchical.distance[node_pair]
                        hierarchical.bestLeft = self.name
                        hierarchical.bestRight = next_node.name


        hierarchical.nodes[self.name] = self   # Finally, add this new instance to the class' static nodes container


    def L2(self, next_node):
        """
            Calculate the L2/euclidean distance between the current instane of the class
            and another instance
        """
        x_vector = self.data #current instance
        y_vector = next_node.data #Other instance

        deltas = sum([(x_vector[i] - y_vector[i])**2 for i in range(len(x_vector))])

        return -sqrt(deltas)

    def single(self, next_node):
        low = -999
        for x in self.represented:
            for y in next_node.represented:
                if hierarchical.distance[x,y] > low:
                    low = hierarchical.distance[x,y]
        return low
    def complete(self, next_node):
        low = 999
        for x in self.represented:
            for y in next_node.represented:
                if hierarchical.distance[x,y] < low:
                    low = hierarchical.distance[x,y]
        return low


    @staticmethod
    def DFS(root,xs,ys):

        if root is not None:

            if root.left:
                hierarchical.DFS(hierarchical.nodes[root.left],xs,ys)
            if root.right:
                hierarchical.DFS(hierarchical.nodes[root.right],xs,ys)

            if root.name.startswith("V"):

                xs.append(root.name)
                ys.append(root.data)
            else:
                pass


    @staticmethod
    def average(x, y):

        return [(x[i] + y[i]) / 2 for i in range(len(x))]

    @staticmethod
    def Cluster():  # This creates a number of composite nodes corresponding to the number of gene nodes less 1

        for i in range(len(hierarchical.nodes) - 1): #n-1

            hierarchical.nodes[hierarchical.bestLeft].taken = True
            # First, mark as taken the nodes to the left and right we are about to join
            hierarchical.nodes[hierarchical.bestRight].taken = True

            leftData = hierarchical.nodes[hierarchical.bestLeft].data 
            rightData = hierarchical.nodes[hierarchical.bestRight].data 
            
            tempdata = hierarchical.average(leftData, rightData)


            tempname = "NODE" + str(i)
            print(tempname)
            hierarchical.metric = 'Complete'

            hierarchical(tempname, tempdata, hierarchical.metric, hierarchical.bestLeft, hierarchical.bestRight, represented= hierarchical.nodes[hierarchical.bestLeft].represented + hierarchical.nodes[hierarchical.bestRight].represented) # + hierarchical.nodes[hierarchical.bestRight].represented)


            hierarchical.bestDistance = hierarchical.dummy #-999999
            #print "hierarchical.distance dict ", hierarchical.distance
            for node_pair, cur_distance in hierarchical.distance.items():

                if cur_distance > hierarchical.bestDistance:
                    left_one, right_one = node_pair
                    if (hierarchical.nodes[left_one].taken is False) and (hierarchical.nodes[right_one].taken is False):
                        #testing to make sure that we are only considering unpaired "available" node pairs
                        hierarchical.bestDistance = cur_distance
                        hierarchical.bestLeft = left_one
                        hierarchical.bestRight = right_one
                        #Reset the class attributes tracking the node pair resulting in the minimal distance

        
        print("Y'all been clustered")
        return



def main():

    points = []
    for x in range(20):
        set1 = np.random.normal(5, 2, 5)
        set2 = np.random.normal(20, 2, 5)
        points.append(list(set1))
        points.append(list(set2))


    for i,vec in enumerate(points):
        hierarchical("Vector" + str(i), vec, metric='Euclidian')

    hierarchical.Cluster()
    global xs
    global ys
    xs = []
    ys = []
    hierarchical.DFS(hierarchical.nodes["NODE37"])
    print(xs)
    print(ys)


    fig, ax = plt.subplots()
    ax.set_yticks(np.arange(len(xs)))
    ax.set_yticklabels(xs)
    im = ax.imshow(ys)
    plt.show()


if __name__ == '__main__':
    main()