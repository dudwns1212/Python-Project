student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
student_scores_sum = sum(student_scores)
print(student_scores_sum)
score_sum = 0
for students_score in student_scores:
    score_sum += students_score
print(score_sum)

max_score = 0
for student_score in student_scores:
    if student_score > max_score:
        max_score = student_score
    print(f"현재 가장 큰 점수 : ${max_score}")

min_score = 99999
for student_score in student_scores:
    if student_score < min_score:
        min_score = student_score
    print(f"현재 가장 작은 점수 : ${min_score}")
