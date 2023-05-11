# Adaline neural network
import numpy as np


def Adaline(Input, Target, lr=0.2, stop=0.001):
    weight = np.random.random(Input.shape[1])  ## משקולות לכל פרמטר אפשרי
    bias = np.random.random(1)  ## b
    Error = [stop + 1]
    # check the stop condition for the network
    while Error[-1] > stop:
        eg = (Error[-1])
        error = []
        for i in range(Input.shape[0]):
            Y_pred   = sum(weight * Input[i]) + bias
            # Update the weight
            for j in range(Input.shape[1]):
                weight[j] = weight[j] + lr * (Target[i] - Y_pred) * Input[i][j]

            # Update the bias
            bias = bias + lr * (Target[i] - Y_pred)

            # Store squared error value
            error.append((Target[i] - Y_pred) ** 2)
        # Store sum of square errors
        Error.append(sum(error))   ## בכל אפוק - אנחנו נסכום את הסכום של הטעיות שיצא לנו במעבר על כל דגימה באימון - אם הסכום הכולל יהיה קטן מערך כלשהו - נדע לעצור
        print('Error :', Error[-1])
    return weight, bias
