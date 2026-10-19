
# Day 11: Python Lists

# Store student marks in a list
marks = [78, 85, 92, 67, 88]

print("Original marks:", marks)

# Access an item
print("First mark:", marks[0])

# Add a new mark
marks.append(95)
print("After adding a mark:", marks)

# Remove a mark
marks.remove(67)
print("After removing 67:", marks)

# Sort marks
marks.sort()
print("Sorted marks:", marks)

# Calculate average
average = sum(marks) / len(marks)
print("Average marks:", round(average, 2))

# Find highest and lowest marks
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
