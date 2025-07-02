class Student:
    def __init__(self, a, b):
        self.name = a
        self.score = b

    def __add__(self, other):
        return self.score + other.score

    def __sub__(self, other):
        return self.score - other.score

    def __mul__(self, other):
        return self.score * other.score

    def __truediv__(self, other):
        return self.score / other.score

    def __floordiv__(self, other):
        return self.score // other.score

    def __mod__(self, other):
        return self.score % other.score

    def __pow__(self, other):
        return self.score ** other.score

    def __eq__(self, other):
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __str__(self):
        return f"Student name is = {self.name} , Its scoreis = {self.score})"

    # def __repr__(self):
    #     return f"Student(name='{self.name}', score={self.score})"
    
    # diffderent for str
    # def __add__(self, other):
    #     return self.name + other.name

    # def __sub__(self, other):
    #     return self.name - other.name

    # def __mul__(self, other):
    #     return self.name * other.score


    # def __pow__(self, other):
    #     return self.name ** other.name

    # def __eq__(self, other):
    #     return self.name == other.name

    # def __ne__(self, other):
    #     return self.name != other.name

    # def __lt__(self, other):
    #     return self.name < other.neme

    # def __le__(self, other):
    #     return self.name <= other.name

    # def __gt__(self, other):
    #     return self.name > other.name

 
s1 = Student("Alice", 80)
s2 = Student("Bob", 70)

print(s1 + s2)      # 150
print(s1 - s2)      # 10
print(s1 * s2)      # 5600
print(s1 / s2)      # 1.142857...
print(s1 == s2)     # False
print(s1 > s2)      # True
print(s1)           # Student(name=Alice, score=80)
