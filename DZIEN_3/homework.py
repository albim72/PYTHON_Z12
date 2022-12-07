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

class Exam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0<=value<=100):
            raise ValueError('ocena musi zawierać się w zakresie: 0-100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self,value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value


albert = Exam()
albert.writing_grade = 82
albert.math_grade = 76

assert albert.writing_grade == 82
assert albert.math_grade == 76
