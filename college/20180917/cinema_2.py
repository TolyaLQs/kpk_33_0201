from cinema import Human, Hall, Cachbox, Pub

# students = Student.import_from_file('students.src')
# [print(el) for el in students]


watcher = Human.import_from_file('human.src')
cachbox = Cachbox.import_from_file('films.src')
hall = Hall.import_from_file('hall.src')
pub = Pub.import_from_file('pub.src')



[print(el) for el in watcher]
[print(el) for el in cachbox]
[print(el) for el in hall]
[print(el) for el in pub]



# group_23.add_students(students_23)
# [print(el, el.group) for el in students_23]

# print('*' * 25)
# students_33 = Student.import_from_file('33_group.src')
# group_33 = Group('33', 'Прикладная информатика 09.02.05')
# group_33.add_students(students_33)
# [print(el, el.group) for el in students_33]
#
# print('*' * 25)
# teachers = Teacher.import_from_file('teacher.src')
# [print(el) for el in teachers]