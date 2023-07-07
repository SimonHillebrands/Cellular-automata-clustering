import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from sklearn.cluster import MiniBatchKMeans

from sklearn.cluster import KMeans


f = open("features2.txt", "r")
lines = f.readlines()
f.close()

X = []
y = []
for line in lines:
    feature = line.split(" : ") 
    name = feature[0]
    feature = feature[1].replace("\n","").replace("[","").replace("]","").split(",")
    feature = [float(i) for i in feature]
    # feature.pop(0)

    X.append(feature)
    y.append(name)


X = np.array(X)
y = np.array(y)

from sklearn.preprocessing import MaxAbsScaler
transformer = MaxAbsScaler().fit(X)
X = transformer.transform(X)
#Elbow plot
# Sum_of_squared_distances = []
# K = range(1,10)
# for num_clusters in K :
#     kmeans = KMeans(n_clusters=num_clusters)
#     kmeans.fit(X)
#     Sum_of_squared_distances.append(kmeans.inertia_)
# plt.plot(K,Sum_of_squared_distances, 'bx-')
# plt.xlabel("Values of K") 
# plt.ylabel("Sum of squared distances/Inertia") 
# plt.title("Elbow Method For Optimal k")
# plt.show()

#Initialize the class object
kmeans = KMeans(n_clusters= 6)
 
#predict the labels of clusters.
label = kmeans.fit_predict(X)
 
#Getting unique labels
 
u_labels = np.unique(label)
 
for i in range(len(label)):
    print(str(label[i]) + " : " + y[i])


#plotting the results:

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('Entropy')
ax.set_ylabel('Area mean')
ax.set_zlabel('Num Clusters Std')

for i in u_labels:
    ax.scatter(X[label == i , 1] , X[label == i , 3] , X[label ==i, 0], label = i)
    #plt.scatter(X[label == i , 0] , X[label == i , 1] , X[label ==i, 2], label = i)
plt.legend()
plt.show()