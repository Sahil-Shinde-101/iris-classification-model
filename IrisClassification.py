import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, confusion_matrix, accuracy_score, precision_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt

data_frame = pd.read_csv('Iris.csv')

X = data_frame.drop('species',axis=1)
Y = data_frame['species']

encoder = LabelEncoder()

Y = encoder.fit_transform(Y)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

sepal_length = float(input("Enter Sepal Length: "))
sepal_width = float(input("Enter Sepal Width: "))
petal_length = float(input("Enter Petal Length: "))
petal_width = float(input("Enter Petal Width: "))

confusion = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix: {confusion}\n")

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy Score: {accuracy}\n")

precision = precision_score(y_test, y_pred, average='weighted')
print(f"Precision Score: {precision}\n")

F1Score = f1_score(y_test, y_pred, average='weighted')
print(f"F1 Score: {F1Score}")

output = model.predict(pd.DataFrame([[sepal_length,sepal_width,petal_length,petal_width]], columns=['sepal_length','sepal_width','petal_length','petal_width']))
output_label = encoder.inverse_transform(output)
print(output_label)

species_names = encoder.classes_
cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d', xticklabels=species_names, yticklabels=species_names, cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()