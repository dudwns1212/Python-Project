# 기존의 코드
numbers = [1,2,3]
new_list = []

for n in numbers:
    add_1 = n+1
    new_list.append(add_1)

print(new_list) # [2,3,4]

# 리스트 컴프리헨션을 사용하는 방법
new_numbers = [item+1 for item in numbers]
print(new_numbers) # [2,3,4]

name = "Angela"
new_name = [letter for letter in name]
print(new_name) # ['A', 'n', 'g', 'e', 'l', 'a']

ex_1 = [n*2 for n in range(1,5)]
print(ex_1) # [2,4,6,8]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie" ]
# 4글자 이하로 구성
new_names = [new_name for new_name in names if len(new_name) < 5]
print(new_names) # ["Alex", "Beth", "Dave"]

# 5글자 이상, 모두 대문자
ex_2 = [new_name.upper() for new_name in names if len(new_name) >= 5]
print(ex_2) # ['CAROLINE', 'ELANOR', 'FREDDIE']

# 딕셔너리 컴프리헨션
import random
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

# 딕셔너리를 활용한 컴프리헨션
passed_students = {student:score for(student, score) in students_scores.items() if score > 60}
print(passed_students)

# 데이터프레임 반복
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for(key, value) in student_data_frame.items():
    print(key)
    print(value)

for(index, row) in student_data_frame.iterrows():
    if index == 1:
        print(row.score)