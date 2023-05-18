import numpy as np
from numpy.linalg import norm
from numpy import dot

def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

def main():
    
    Docs = np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
    Query = np.array([1,1,0,0,1,0])
    
    doc1 = cos_sim(Docs[0],Query)
    doc2 = cos_sim(Docs[1],Query)
    doc3 = cos_sim(Docs[2],Query)
    
    print("doc1={0:.2f}".format(doc1))
    print("doc2={0:.2f}".format(doc2))    
    print("doc3={0:.2f}".format(doc3)) 
    
if __name__ == "__main__":
    main()