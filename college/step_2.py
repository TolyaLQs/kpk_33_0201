from college import Human, Student, Group

student_1 =Student('Петр', 'Игнатьев', 'Ильич')
student_2 =Student('Анна', 'Воробьева', 'Кирилловна')
student_3 =Student('Кирил', 'Мешков', 'Павлович')
student_4 =Student('Света', 'Дудкина', 'Денисовна')
student_5 =Student('Влад', 'Лотарев', 'Викторович')

# print(student_1)

group_1 = Group('33', 'Прикладная информатика 09.02.05')
group_2 = Group('23', 'Прикладная информатика 09.02.05')
# print()

# student_1.set_group('33')
student_1.set_group(group_1)
student_2.set_group(group_1)
student_3.set_group(group_1)
student_4.set_group(group_2)
student_5.set_group(group_2)

students = [student_1, student_2,student_3, student_4, student_5]

# print(student_1.group)
print(f'\nВ мероприятии участвовали: ')
for student in students:
    print(f'{student} ({student.group})')
