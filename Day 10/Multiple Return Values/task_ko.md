함수는 `return` 키워드에서 종료됩니다. `return` 문 아래에 코드를 작성하면 해당 코드는 실행되지 않습니다.

하지만, 하나의 함수에 여러 개의 `return` 문을 가질 수 있습니다. 그렇다면 이것이 어떻게 작동할까요?

### 조건부 반환

조건부 흐름 제어(코드가 특정 조건 검사에 따라 다르게 동작하여 다른 실행 경로를 따르는 경우)가 있을 때, 여러 가지 종료점(`return`)이 생길 수 있습니다.

예:
```
def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
```

### 빈 반환
`return` 뒤에 아무 것도 작성하지 않고 반환할 수도 있습니다. 이것은 단순히 함수에게 종료하라고 지시합니다.

예:
```
def canBuyAlcohol(age):
    # age 입력의 데이터 타입이 int가 아니면 종료합니다.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False