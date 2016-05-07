#!/usr/bin/python
import sys
import csv
import random
import numpy
def dataread(filename):
	with open(filename , 'rb') as csvfile:
		read = csv.reader(csvfile , delimiter=',')
		data = []
		for i in read:
			data.append(i)
	return data

def distance(x,y):
	return numpy.sqrt(numpy.sum((x-y)**2))


def compute( datavector , mean_centers):
	min_dist = 100000
	ind = 0
	datavector = map( float , datavector)
	a = numpy.array(datavector)
	#print a
	for i in range(len(mean_centers)):
	#	mean_centers[i] = map( float , mean_centers[i])
		b = numpy.array(mean_centers[i])
	#	print b
		dist = distance(a,b)
		if(dist < min_dist):
			min_dist = dist
			ind = i
	return ind

def mean( cluster  , dataset ):
	total_sum = [ 0 for i in range(4)]
	for i in range(len(cluster)):
		data = dataset[cluster[i]][0:4]
		a = map( float , data)
		a = numpy.array(a)
		total_sum = total_sum + a
	total_sum = total_sum / len(cluster)
	return total_sum

def computeError( a , b):
	#print a 
	#print b
	err  = 0
	for i in range(len(a)):
		b[i] = numpy.array(b[i])
		err = err + sum(a[i] - b[i])
	return err






def kmeans( dataset , no_of_clusters):
    mean_centers = []
    temp_centers = []
    size = len(dataset)
    index = [ i for i in range(size)]
    index = random.sample(index , no_of_clusters)
    print index
    for j in range(no_of_clusters):
    	mean_centers.append(dataset[index[j]][0:4])
    	mean_centers[j] = map( float , mean_centers[j])
    print mean_centers
    
    error = 0
    while 1:
    	clusters = []
    	for i in range(no_of_clusters):
    		clusters.append([])
    	for i in range(size):
    #		print i
    		closest_cluster = compute(dataset[i][0:4] , mean_centers  )
    		#print closest_cluster
    		clusters[closest_cluster].append(i)
    	for i in range(no_of_clusters):
    		temp_centers.append([])
    		temp_centers[i] = mean(clusters[i] , dataset)
    #	print 'Hello\n'
        error = computeError(temp_centers , mean_centers)

        #print erro
    	if(abs(error) == 0 ):
    	    break
    	for i in range(no_of_clusters):
        	mean_centers[i] = temp_centers[i]
        temp_centers = []
        for i in range(no_of_clusters):
        	print len(clusters[i])
        print '\n'


   # print clusters
   # print mean_centers






# Arg1 for dataset and Arg2 for number of clusters
data = dataread(str(sys.argv[1]))
kmeans(data , int(sys.argv[2]))


#print type(data)
#print data