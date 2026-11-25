# Day 37 - Decision Tree vs Random Forest

## Aim
To understand and compare Decision Tree and Random Forest classification algorithms.

## What is a Decision Tree?
A Decision Tree makes a prediction by asking a series of questions about the data. It looks like a tree with branches.

## What is Random Forest?
Random Forest creates many decision trees and combines their predictions. This often gives more stable results than using only one tree.

## Dataset
This program uses the built-in Iris flower dataset from scikit-learn. It contains measurements of flowers from three Iris species.

## Libraries Used
- scikit-learn

## How to Run
1. Install Python.
2. Install the required library:

   ```bash
   pip install scikit-learn
   ```

3. Run the program:

   ```bash
   python decision_tree_vs_random_forest.py
   ```

## Expected Output
The program displays the accuracy and classification report for both models, then predicts the flower type for one sample. Exact results may vary if the dataset or settings are changed.

## What I Learned
- How a Decision Tree works.
- How Random Forest combines multiple trees.
- How to train and test classification models.
- How to compare models using accuracy.

## Note
This is a learning exercise using the Iris dataset. Accuracy on this small, standard dataset does not guarantee performance on other real-world data.
