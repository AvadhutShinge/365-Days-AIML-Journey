# Day 36 – Student Performance Prediction using Naive Bayes

## Objective
Build a beginner-friendly machine learning classifier that predicts whether a student may pass or fail using study hours and attendance.

## Algorithm
Gaussian Naive Bayes (GaussianNB), a probability-based classification algorithm.

## Features
- Study hours per day
- Attendance percentage

## Target Labels
- 0 – Fail
- 1 – Pass

## Technologies
- Python
- Scikit-learn

## Installation
Install the required library:

```bash
pip install scikit-learn
```

## Run
```bash
python naive_bayes.py
```

The program splits the sample data into training and testing sets, trains a Gaussian Naive Bayes model, displays accuracy and a classification report, and predicts the result for a sample student.

## Learning Outcome
Learned how to train and evaluate a Naive Bayes classification model using Python.

## Note
This is a small illustrative dataset for learning. Its predictions are not a reliable assessment of real student performance. A larger, representative real-world dataset is needed for meaningful use.
