# Day 38 - Classification Model Evaluation

## Aim
To evaluate a machine learning classification model using common performance metrics.

## Concepts Covered
- **Accuracy:** The proportion of all predictions that are correct.
- **Precision:** Of the samples predicted as a class, how many were correct.
- **Recall:** Of the actual samples in a class, how many were correctly identified.
- **F1-score:** The harmonic mean of precision and recall.
- **Confusion Matrix:** A table that compares actual classes with predicted classes.

## Dataset
This program uses the built-in Iris flower dataset from Scikit-learn. It contains 150 flower samples from three species.

## Model Used
Random Forest Classifier with 100 decision trees.

## Libraries Used
- scikit-learn

## Installation
```bash
pip install scikit-learn
```

## Run the Program
```bash
python classification_evaluation.py
```

## Output
The program displays accuracy, macro-averaged precision, recall, F1-score, a confusion matrix, a classification report, and a sample flower prediction.

## What I Learned
- How to evaluate a classification model.
- The difference between accuracy, precision, recall, and F1-score.
- How to read a confusion matrix.
- Why multiple evaluation metrics are useful when checking a model.

## Note
The Iris dataset is a small educational dataset. A high score on this dataset does not guarantee similar performance on real-world data.
