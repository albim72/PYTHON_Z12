from weakref import WeakKeyDictionary

#przypadek 0

class Grade:
    def __get__(self,instance,instance_type):
        pass

    def __set__(self, instance, value):
        pass

class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

exam = Exam()
exam.writing_grade = 45

Exam.__dict__['writing_grade'].__set__(exam,40)
exam.writing_grade

#Exam.__dict__['writing_grade'].__set__(exam,Exam)
Exam.__dict__['writing_grade'].__get__(exam,Exam)

#przypadek 1


class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self,instance,instance_type):
        if instance is None:
            return self
        return self._values.get(instance,0)

    def __set__(self, instance, value):
        if not (0<=value<=100):
            raise ValueError('ocena musi być z zakresu: 0-100')
        self._values[instance]=value

class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

fexam = Exam()
fexam.writing_grade = 99
gexam = Exam()
gexam.writing_grade = 71
print(f'pierwszy egzamin: {fexam.writing_grade}')
print(f'drugi egzamin: {gexam.writing_grade}')
