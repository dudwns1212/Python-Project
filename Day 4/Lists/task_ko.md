간단한 정렬된 항목 모음을 Python 리스트를 사용해 생성할 수 있습니다. 예:

`fruits = ["Cherry", "Apple", "Pear"]`

또는

`states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]`

### 리스트의 항목 접근하기

리스트 이름을 적고 대괄호 안에 접근하려는 항목의 인덱스를 입력하여 항목에 접근할 수 있습니다. 예:

`states_of_america[0]`

위 코드는 "Delaware"를 반환합니다.

컴퓨터와 관련된 모든 것에서, 숫자를 셀 때 첫 번째 번호는 항상 0부터 시작하며, 1부터가 아닙니다. 따라서 0, 1, 2, 3 대신 1, 2, 3, 4가 아닙니다.

### 음수 인덱스

리스트의 끝에서부터 항목을 접근하려면 음수 정수를 사용할 수 있습니다. 예:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] # 이것은 "Pear"를 반환합니다
```

### 항목 수정하기

리스트의 항목을 가져오는 동일한 구문을 사용해 항목을 수정할 수 있습니다. 예:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# fruits는 이제 ["Orange", "Apple", "Pear"]가 됩니다
```

### 항목 추가하기

리스트의 끝에 항목을 추가하려면 `append()` 함수를 사용할 수 있습니다. 예:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# fruits는 이제 ["Cherry", "Apple", "Pear", "Orange"]가 됩니다
```

### 리스트 문서화

Python 리스트와 기타 리스트 관련 함수에 대한 문서는 여기에서 확인할 수 있습니다: https://docs.python.org/3/tutorial/datastructures.html