### 중첩 조건문  
if/else 문을 다른 if/else 문 안에 넣을 수 있습니다. 이를 중첩(nesting)이라고 합니다.  
예시:  

```
if maths_score >= 90:
    if english_score >= 90:
        print("당신은 모든 과목을 잘합니다.")
    else:
        print("당신은 수학을 잘합니다.")
if english_score >= 90:
    print("당신은 영어를 잘합니다.")
```

이 경우, 학생이 수학과 영어 모두 90점을 넘긴 경우에만 "당신은 모든 과목을 잘합니다."라는 메시지를 받을 수 있습니다.  

참고: else 문과 짝이 없는 독립적인 if 문도 사용할 수 있습니다.