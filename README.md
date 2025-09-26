# iris-classification-model
This project implements a Logistic Regression model to classify flowers in the Iris dataset into three species: Setosa, Versicolor, and Virginica. The model achieves high accuracy (≈100% with random_state=42), making it reliable for classification tasks on the Iris dataset.

Iris Flower Classification using Logistic Regression

This project implements a Logistic Regression model to classify the famous Iris dataset
 into three species:

*Setosa

*Versicolor

*Virginica

It demonstrates a full machine learning workflow including data preprocessing, model training, evaluation, and predictions.

## Project Structure:

├── Iris.csv                # Dataset

├── IrisClassification.py    # Main Python code

├──requirements.txt          #Requirements file

├── README.md               # Project documentation




## Features:

Data preprocessing with Label Encoding

Train-test split with scikit-learn

Logistic Regression model training

Model evaluation using:

Confusion Matrix

Accuracy

Precision

F1 Score

Prediction on new custom inputs with actual species name output

Optional: confusion matrix heatmap visualization

## Installation:
### 1.Clone this repo:
git clone https://github.com/Sahil-Shinde-101/iris-classification-model.git

cd iris-classification-model

### 2.Install dependencies:
pip install -r requirements.txt

## Usage:
### 1.Run the file:

python SpeciesPrediction.py

### 2.Sample output:

Enter Sepal Length: 6.9

Enter Sepal Width: 3.1

Enter Petal Length: 5.1

Enter Petal Width: 2.3

#### Confusion Matrix:

 [[10  0  0]
 
 [ 0  9  0]
 
 [ 0  0 11]]

Accuracy Score: 1.0

Precision Score: 1.0

F1 Score: 1.0

['virginica']

## Example Confusion Matrix Heatmap:



<img width="768" height="587" alt="Screenshot 2025-09-26 105004" src="https://github.com/user-attachments/assets/67e2b7db-08d8-4ba0-a9d8-600a402c59bb" />


## Flowchart of Pipeline I created:


<img width="740" height="607" alt="Screenshot 2025-09-26 111258" src="https://github.com/user-attachments/assets/8e824afa-71c2-4092-afa4-68afc77e0730" />
