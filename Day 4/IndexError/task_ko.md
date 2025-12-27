### 리스트의 길이
`len()` 함수를 사용하여 리스트의 길이(리스트에 있는 항목의 수)나 문자열의 길이(문자열의 문자 수)를 구할 수 있습니다. https://docs.python.org/3/library/functions.html#len

### IndexError
리스트 범위에 없는 항목에 접근하려고 하면 `IndexError`가 발생합니다. 예:

```
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3]) #이 코드는 IndexError를 발생시킵니다
```

### 중첩 리스트
리스트 안에 다른 리스트를 넣을 수 있으며, 이를 "중첩 리스트" 또는 "2차원 리스트"라고 합니다. 예:

```
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#리스트는 다음과 같은 모양이 됩니다: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
```

또한 이렇게 2D 형식으로 리스트를 표현할 수도 있습니다:
```
["Cherry", "Apple", "Pear"]
["Cucumber", "Kale", "Spinnach"]