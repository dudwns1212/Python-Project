### 여러 개의 입력값  
함수에 여러 개의 입력값을 사용할 수 있습니다. 필요한 것은 각 입력값을 쉼표 `,`로 구분하는 것뿐입니다.

### PAUSE 1  
여러 개의 입력값을 가진 함수를 만들어 보세요.

<div class="hint">
  <code>
def greet(name, greeting):

    ____print(f"{greeting} {name}")
    
greet("Angela", "Yo!")
</code>
</div>

### PAUSE 2  
함수를 수정하여 예상 값을 출력하도록 만드세요.
```
def greet_with(name, location)
    Hello name
    What is it like in location
```

### 위치 기반 인수  
기본적으로 Python에서 함수를 생성하면 함수 정의에서 인수들의 순서를 유지합니다.

예: 아래의 함수에서 첫 번째로 전달받은 인수는 항상 두 번째 인수보다 먼저 출력됩니다. `a = 2, b = 1`

```
def my_function(a, b)
  print(a)
  print(b)
  
my_function(2, 1)
#출력 결과는:
# 2
# 1
```

### 키워드 인수  
함수를 호출할 때 인수를 제공할 때 키워드를 사용할 수 있으며, 이를 통해 어떤 값이 어떤 입력 매개변수에 할당되는지에 대한 혼동을 줄일 수 있습니다.

### PAUSE 3  
`greet_with()` 함수를 키워드 인수를 사용하여 호출하세요.

<div class="hint">
  <code>
greet_with(location="London", name="Angela")
</code>
</div>