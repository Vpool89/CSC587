import numpy as np

#using numpy calculate the manhattan distance of i and j via calculating the sum of the absolute difference
def manhattan_distance(p1, p2):
    return np.sum(np.abs(np.array(p1)- np.array(p2)))
#using numpy calculate the euclidean distance using np lineralgebra and normal which calculates the euclidean distance 
def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1)-np.array(p2))

#test 3d Vectors 
test_vector1 = [1,2,3]
test_vector2 = [4,5,6]

#test 2d points 
p1 = [1,1]
p2 = [2,2]


#compute the distance 

#distance = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
print("\nTest Vectors enter: i(",test_vector1[0],",",test_vector1[1],",",test_vector1[2],") &  j(",test_vector2[0],",",test_vector2[1],",",test_vector2[2],")")
print("Euclidean distance")
print(euclidean_distance(test_vector1,test_vector2))
print("Manhattan Distance")
print(manhattan_distance(test_vector1, test_vector2))
print("\nTest Vectors enter: i(",p1[0],",",p1[1],") & j(",p2[0],",",p2[1],")")
print("Euclidean distance")
print(euclidean_distance(p1,p2))
print("Manhattan Distance")
print(manhattan_distance(p1,p2))
