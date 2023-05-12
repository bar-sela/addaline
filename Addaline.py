# Adaline neural network
import numpy as np
from sklearn.model_selection import KFold


def Adaline(Input, Target, lr=0.02, stop=0.001):
    kfold = KFold(n_splits=5, shuffle=True, random_state=42)
    for train_index, val_index in kfold.split(Input):
        X_train, X_val = Input[train_index], Input[val_index]
        y_train, y_val = Target[train_index], Target[val_index]

        weight = np.random.random(X_train.shape[1])  ## משקולות לכל פרמטר אפשרי
        bias = np.random.random(1)  ## b
        Error = [stop + 1]
        # check the stop condition for the network
        while Error[-1] > stop:
            eg = (Error[-1])
            error = []
            for i in range(X_train.shape[0]):  ## מעבר על כל הדגימות
                Y_pred   = sum(weight * X_train[i]) + bias
                # Update the weight
                for j in range(100):
                    print(j)
                    weight[j] = weight[j] + lr * (y_train[i] - Y_pred) * X_train[i][j]
                    if j == 99 :
                        s  = 2
                # Update the bias
                bias = bias + lr * (X_val[i] - Y_pred)

                # Store squared error value
                error.append((X_val[i] - Y_pred) ** 2)
            # Store sum of square errors
            Error.append(sum(error))   ## בכל אפוק - אנחנו נסכום את הסכום של הטעיות שיצא לנו במעבר על כל דגימה באימון - אם הסכום הכולל יהיה קטן מערך כלשהו - נדע לעצור
            print('Error :', Error[-1])
    return weight, bias
