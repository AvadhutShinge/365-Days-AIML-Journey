# Day 39 - K-Nearest Neighbors (KNN) Classification

## Aim
To understand and implement the K-Nearest Neighbors algorithm for classifying Iris flowers.

## What is KNN?
K-Nearest Neighbors is a supervised machine learning algorithm. It predicts the class of a new data point by finding the K closest training points and choosing the most common class among them.

## Dataset
This practical uses the built-in Iris dataset from Scikit-learn. It contains measurements of 150 flowers from three Iris species.

## Steps Performed
1. Load the Iris dataset.
2. Split the data into training and testing sets.
3. Scale the features using StandardScaler.
4. Train KNN models with K values 3, 5, and 7.
5. Compare their accuracy and classification reports.
6. Train a final model with K = 5 and predict a sample flower.

## Libraries Used
- scikit-learn

## Installation
```bash
pip install scikit-learn
```

## Run the Program
```bash
python knn_classification.py
```

## What I Learned
- The basic working of the KNN algorithm.
- Why feature scaling is important for distance-based algorithms.
- How different K values can affect classification.
- How to evaluate a classification model using accuracy and a classification report.

## Note
The Iris dataset is a small educational dataset. Results on it do not guarantee the same performance on real-world datasets.
