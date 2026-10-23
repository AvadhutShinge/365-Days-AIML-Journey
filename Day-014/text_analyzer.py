

text = input("Enter a sentence: ")

# Count characters and words
characters = len(text)
words = len(text.split())

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print("\n--- Text Analysis ---")
print("Original text:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Character count:", characters)
print("Word count:", words)
print("Vowel count:", vowel_count)
print("Replaced spaces:", text.replace(" ", "-"))

# Check palindrome after removing spaces
clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")
