import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
x = pd.DataFrame(iris.data, columns=[iris.feature_names])
y = pd.Series(iris.target)

# print("Independent Variables:\n", x.head())
# print("\nDependent Variables:\n", y.head())
# print("\nClasses/Categories number:\n", y.value_counts())

import keras

y = keras.utils.to_categorical(y, num_classes=3)
print("\nDependent Variables One Hot Encoded:\n", y)
