다양한 데이터 유형을 결합하여 원하는 구조를 만들 수 있습니다.

### 딕셔너리 안에 리스트 중첩하기
키에 할당된 값을 문자열 대신 리스트로 대체할 수 있습니다. 딕셔너리 안에 리스트를 다음과 같이 중첩할 수 있습니다:

```
my_dictionary = {
    key1: [List],
    key2: Value,
}
```

### 일시정지 1
중첩된 리스트 `travel_log`에서 "Lille"을 출력하는 방법을 찾아보세요.
```
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
```
<div class="hint">
  이 부분을 얻으려면: <code>["Paris", "Lille", "Dijon"]</code>
<code>travel_log["France"]</code>가 필요합니다.

따라서 "Lille"을 얻으려면:
<code>travel_log["France"][1]</code>
</div>

### 리스트 안에 다른 리스트 중첩하기

이전에 중첩된 리스트를 살펴보았습니다:

```
nested_list = ["A", "B", ["C", "D"]]
```

### 일시정지 2
깊이 중첩된 리스트 항목을 얻는 방법을 기억하시나요? 리스트 `nested_list`에서 "D"를 출력해보세요.

<div class="hint">
  이 리스트를 얻기 위해서는: ["C", "D"] 아래 코드가 필요합니다:

<code>nested_list[2]</code>

따라서 "D"를 얻으려면:

<code>nested_list[2][1]</code>
</div>


### 딕셔너리 안에 딕셔너리 중첩하기
딕셔너리 안에 딕셔너리를 중첩할 수도 있습니다:

```
my_dictionary = {
    key1: Value,
    key2: {Key: Value, Key: Value},
}
```

### 일시정지 3
다음 리스트에서 "Stuttgart"를 출력하는 방법을 찾아보세요:
```
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}