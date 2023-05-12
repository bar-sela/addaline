# Import necessary libraries
import numpy as np

import Addaline
import ast
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
    NumOfOnce = 5
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
    listOfVectors = []
    listOfAllTags = []
    # Load the vector from the file as a string
    with open(file_path, 'r') as file:
        s = file.readline()
        counter = 0
        while(s ) :
            curString = s
            sToList  = ast.literal_eval(s)  ### ממיר את הווקטור שנקרא כמחרוזת לרשימה בפייתון עם מספרים שלמים
            s = file.readline()
            if not Exclude_uncorrect_vectors(sToList):
                 continue
            listOfAllTags.append(float(curString[1]))
            listOfVectors.append(sToList)
    print(len(listOfVectors))
    return listOfVectors,listOfAllTags

def DeleteFirstVariable(listOfLists):
      for i in range(0, len(listOfLists)) :
          listOfLists[i] = listOfLists[i][1:]
if __name__ == "__main__":
    print("start Algorithem : BET and Lamed")
    listOfGoodVec,listOfAllTags = loop_and_extractGoodVectors()

    listOfBetAndMem = list(filter(lambda x:True if x[0] != 3 else False,listOfGoodVec ))
    DeleteFirstVariable(listOfBetAndMem)
    listOfBetAndMem =  np.array(listOfBetAndMem )
    tagsBetAndMem =  list(filter(lambda x: True if x != 3 else False, listOfAllTags))
    tagsBetAndMem= np.array(tagsBetAndMem)
    Addaline.Adaline(listOfBetAndMem,tagsBetAndMem)




    """
    listOfBetAndLamed =  list(filter(lambda x:True if x[0] != 2 else False,listOfGoodVec ))
    listOfBetAndLamed =  np.array(listOfBetAndLamed[1:] )
    tagsBetAndLamed =  list(filter(lambda x: True if x != 2 else False, listOfAllTags))
    tagsBetAndLamed = np.array(tagsBetAndLamed)

    listOfMemAndLamed =  list(filter(lambda x:True if x[0] != 1 else False,listOfGoodVec ))
    listOfMemAndLamed=  np.array(listOfBetAndMem[1:] )
    tagsMemAndLamed =  list(filter(lambda x: True if x != 1 else False, listOfAllTags))
    tagsMemAndLamed = np.array( tagsMemAndLamed )

    print(len(listOfBetAndMem))
    print(len(listOfMemAndLamed))
    print(len(listOfBetAndLamed))

"""



