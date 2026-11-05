# Data Filtering and Transformation System

# Original dataset
marks = [35, 78, 90, 42, 28, 65, 100, -5]

print("Original Dataset:")
print(marks)


# 1. List Comprehension
# Remove invalid marks

valid_marks = [mark for mark in marks if 0 <= mark <= 100]

print("\nValid Marks:")
print(valid_marks)


# 2. Filter Function
# Select students who passed (marks >= 40)

passed_marks = list(filter(lambda mark: mark >= 40, valid_marks))

print("\nPassed Marks:")
print(passed_marks)


# 3. Map Function
# Add 5 bonus marks (maximum 100)

updated_marks = list(map(lambda mark: min(mark + 5, 100), passed_marks))

print("\nMarks After Adding Bonus:")
print(updated_marks)


# 4. List Comprehension
# Find students with high marks

high_marks = [mark for mark in updated_marks if mark >= 75]

print("\nHigh Marks:")
print(high_marks)


# 5. Calculate Average

average = sum(updated_marks) / len(updated_marks)

print("\nAverage Marks:", round(average, 2))