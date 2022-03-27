import numpy as np
"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return self.name != other.name
    def __lt__(self, other):
        return self.name < other.name
    def __gt__(self, other):
        return self.name > other.name
    def __le__(self, other):
        return self.name <= other.name
    def __ge__(self, other):
        return self.name >= other.name

def main():
    """A simple test."""
    student = Student("Ken", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)

    a = Student("Alice", 5)
    b = Student("Jeremiah", 5)
    print(f"{a.name} is equal to {b.name}: {a==b}")
    print(f"{a.name} is less than to {b.name}: {a<b}")
    print(f"{a.name} is greater than to {b.name}: {a>b}")

    arr = [a, b, Student("Claire", 5), Student("Danny", 5)]
    np.random.shuffle(arr)
    arr = sorted(arr)
    for i, j in enumerate(arr):
        print(f"Element {i+1}: {j.name}")

if __name__ == "__main__":
    main()


