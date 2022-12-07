class Homework:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,value):
        if not(0<=value<=100):
            raise ValueError('ocena musi zawierać się w zakresie: 0-100')
        self._grade = value

galileo = Homework()
galileo.grade = 98
assert galileo.grade == 98
