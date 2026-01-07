당신은 코드에서 `global` 키워드를 사용하여 무언가를 수정할 수 있도록 강제로 허용할 수 있습니다.

예: 이것은 오류를 발생시킵니다

```
a = 1
def my_function():
    a += 1
    print(a)
```

하지만 이렇게 하면 작동합니다
```
a = 1
def my_function():
    global a
    a += 1
    print(a)