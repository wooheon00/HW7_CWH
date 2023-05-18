import numpy as np

def main():
    A = np.array([[1,2],[3,4]])
    evalue, evector = np.linalg.eig(A)
    v1 = np.array([1,2,3])
    v2 = np.array([4,5,6])
    cross = np.cross(v1,v2)
    A1 = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    b = np.array([-15,-21,18])
    x = np.linalg.solve(A1,b)
    print("Eigenvalues: {}, {}".format(evalue[0], evalue[1]))
    print("Eigencevtors: {}, {}". format(evector[0], evector[1]))
    print("Determinant: {0:d}". format(int(np.linalg.det(A))))
    print("Cross product: {}". format(cross))
    print("Solution: {}".format(x))

if __name__ == "__main__":
    main()
