import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# LIST COMPREHENSIONS
doubled = [n * 2 for n in range(1, 5)]
print(doubled)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# DICTIONARY COMPREHENSIONS
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: grade for (student, grade) in students_scores.items() if grade > 50}
print(passed_students)
