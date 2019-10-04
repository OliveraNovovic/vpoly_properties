import numpy as np



def main():
    centroids = "/home/olivera/Documents/data/vpoly_centroids/vpoly_1.txt"
    matrix = []
    with open(centroids, 'r') as cent:
        lines = cent.readlines()
        for line in lines:
            el = line.split(" ")
            lon = float(el[1][1:])
            lat = float(el[2][:-2])
            #zeros = np.zeros((60,), dtype=int)
            coord = [lon, lat]
            for i in range(1, 61):
                coord.append(0.0)
            matrix.append(coord) # we are adding zeros because linalg.eig asks for a square matrix,
                                # in the end we should have matrix of size 62x62 where first two elements are coords

    #print(matrix)

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    print(eigenvectors)
    print(eigenvalues)

    # Calculate dot product
    dot_prod = np.dot(eigenvalues, eigenvectors)
    print(dot_prod)

    #print(eigenvalues)
    #print(eigenvectors)






if __name__=="__main__":
    main()