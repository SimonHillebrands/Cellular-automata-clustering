import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time

#might need to account for the wrap around at some point but this might be fine for now

start = time.time()


dir_list = os.listdir("temp")

frame_count = len(dir_list)
avg_displacement = []

def cluster(path):
    # Load the image
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)


    # Threshold the image to binarize it
    _, thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # Perform connected component analysis to obtain the clusters
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh, connectivity=8)

    # Sort the clusters by size (largest to smallest)
    sizes = stats[:, -1]
    sorted_idxs = np.argsort(sizes)[::-1]
    sorted_labels = np.zeros_like(labels)
    for i, idx in enumerate(sorted_idxs):
        sorted_labels[labels == idx] = i + 1

    # Apply a color map to the labeled image
    num_labels = np.max(sorted_labels) + 1
    colors = plt.cm.get_cmap('rainbow', num_labels)
    colored_labels = colors(sorted_labels)[:, :, :3] * 255
    colored_labels = colored_labels.astype(np.uint8)

    colored_labels = cv2.resize(colored_labels, (0, 0), fx = 3, fy = 3)

    print(set(labels.flatten()))

    return centroids

    #cv2.imwrite("clusters/" + path, colored_labels)
    #return(colored_labels)
prev_centroids = cluster(cv2.os.path.join("temp", dir_list[0]))
dir_list.pop(0)
for i in dir_list:
    centroids = cluster(cv2.os.path.join("temp", i))

    displacement = [np.linalg.norm(centroids[j] - prev_centroids[j]) for j in range(min(len(prev_centroids),len(centroids)))]
    avg_displacement.append(np.mean(displacement[-frame_count:]))

    prev_centroids = centroids
    
    #print("Average displacement:", avg_displacement)

print(np.std(avg_displacement))
end = time.time()

print(end - start)