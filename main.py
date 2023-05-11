# Import necessary libraries
import numpy as np

"""
# Input dataset
x = np.array([[1.0, 1.0, 1.0],
              [1.0, -1.0, 1.0],
              [-1.0, 1.0, 1.0],
              [-1.0, -1.0, -1.0]])
# Target values
t = np.array([1, 1, 1, -1])

w, b = Adaline(x, t, lr=0.2, stop=0.001)
print('weight :', w)
print('Bias :', b)
"""



def Exclude_uncorrect_vectors(vetcor):
    NumOfOnce = 17
    if  len(vetcor) != 101 :
        return  False
    for i in range(0,len(vetcor)):
        if vetcor[i] == 1:
            NumOfOnce-= 1
            if NumOfOnce == 0 :
                return True
    return False
# Specify the file path

def loop_and_extractGoodVectors():
    file_path = 'result.txt'
    l = []
    # Load the vector from the file as a string
    with open(file_path, 'r') as file:
        s = file.readline()
        counter = 0
        while(s ) :
            vector = np.array(eval(s))
            s = file.readline()
            if Exclude_uncorrect_vectors(vector):
                 continue
            l.append(vector)

    return l
if __name__ == "__main__":
    print("start Algorithem : BET and Lamed")
    listOfGoodVec = loop_and_extractGoodVectors()
    listOfBetAndMem = filter(lambda x:True if x[0] != 3 else False,listOfGoodVec )
    print(list(listOfBetAndMem))










