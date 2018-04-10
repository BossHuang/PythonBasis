__author__ = 'leihuang'

class SimpleGradebook(object):
    def __init__(self):
        self._grade = {}
    def add_student(self, name):
        if name not in self._grade:
            self._grade[name] = []
    def report_grade(self, name, score):
        if name not in self._grade:
            self._grade[name] =  []
        self._grade[name].append(score)
    def average_grade(self,name):
        grades = self._grade[name]
        return sum(grades)*1.0/len(grades)


class BySubjectGradebook(object):
    def __init__(self):
        self._grade = {}
    def add_student(self, name):
        if name not in self._grade:
            self._grade[name] = {}
    def report_grade(self, name, subject, score):
        if name not in self._grade:
            self._grade[name] = {}
        by_subject = self._grade[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(score)
    def average_grade(self, name):
        by_subject = self._grade[name]
        total, count = 0.0, 0.0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total/count

class WeightedGradebook(object):
    def __init__(self):
        self._grade = {}
    def add_student(self, name):
        if name not in self._grade:
            self._grade[name] = {}
    def report_grade(self, name, subject, score, weight):
        if name not in self._grade:
            self._grade[name] = {}
        by_subject = self._grade[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score,weight))
    def average_grade(self, name):
        by_subject = self._grade[name]
        total, count = 0.0, 0.0
        for subject in by_subject:
            total_subject, count_subject = 0.0, 0.0
            for score, weight in subject:
                total_subject += score*weight
                count_subject += 1
            total += total_subject
            count += count_subject
        return total/count


import collections
Grade = collections.namedtuple('Grade',('score', 'weight'))

class Subject(object):
    def __init__(self):
        self._grades = []
    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))
    def average_grade(self):
        total, total_weight = 0.0, 0.0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total/total_weight

class Student(object):
    def __init__(self):
        self._subjects = {}
    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]
    def average_grade(self):
        total, count = 0.0, 0.0
        for subject in self._subjects:
            total += self._subjects[subject].average_grade()
            count += 1
        return total/count

class Gradebook(object):
    def __init__(self):
        self._students = {}
    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

book = Gradebook()
albert = book.student('Albert')
math = albert.subject('math')
math.report_grade(score=80, weight=0.10)
print albert.average_grade()
