# Custom Iterator

class NumberIterator:

    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


# Generator Function

def square_generator(numbers):
    for number in numbers:
        yield number * number


# Main Program

numbers = [1, 2, 3, 4, 5]

print("Original Numbers:")

iterator = NumberIterator(numbers)

for number in iterator:
    print(number)

print("\nSquares using Generator:")

for square in square_generator(numbers):
    print(square)