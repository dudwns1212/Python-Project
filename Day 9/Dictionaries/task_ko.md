파이썬에서의 딕셔너리는 실제 생활의 사전과 유사하게 작동합니다. 이는 데이터 구조로, 키를 값과 연결하여 두 데이터를 함께 짝짓는 것이 가능합니다.

다음은 파이썬에서 딕셔너리를 생성하는 방법입니다:
```
# 딕셔너리 예제
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}
```

다음은 딕셔너리에서 항목을 가져오는 방법입니다:
```
print(colours["pear"])
# "green"을 출력합니다
```

다음은 빈 딕셔너리를 생성하는 방법입니다:
```
my_empty_dictionary = {}
```

다음은 기존 딕셔너리에 새 항목을 추가하는 방법입니다:
```
colours["peach"] = "pink"
```

다음은 딕셔너리에 있는 기존 값을 수정하는 방법입니다:
```
colours["apple"] = "green"
```

다음은 딕셔너리를 순회하며 모든 키를 출력하는 방법입니다:
```
for key in colours:
    print(key)
```

다음은 딕셔너리를 순회하며 모든 값을 출력하는 방법입니다:
```
for key in colours:
    print(colours[key])