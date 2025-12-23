### TypeError  
이 오류는 잘못된 데이터 타입을 사용할 때 발생합니다.  
예: `len(12345)`  

`len()` 함수는 문자열(String)만 받을 수 있기 때문에, 숫자(Integer)를 입력하면 작동을 거부하며 TypeError를 발생시킵니다.  

#### 잠깐 멈춤 1. `len()` 함수에서 더 이상 경고나 오류가 발생하지 않도록 수정하세요.  

### 타입 확인  
Python에서 값이나 변수의 데이터 타입을 확인하려면 `type()` 함수를 사용할 수 있습니다.  

`print(type("abc")) #결과는 <class 'str'>`  

#### 잠깐 멈춤 2. 4개의 타입을 확인하는 코드를 작성하세요  
`type()` 함수와 `print()` 함수를 사용해 4줄의 출력을 생성하여 우리가 배운 데이터 타입 4개를 모두 출력하세요. `<class 'str'> <class 'int'> <class 'float'> <class 'bool'>`  

### 타입 변환  
특정 함수를 사용하여 데이터를 다른 데이터 타입으로 변환할 수 있습니다.  
예:  

`float()`  

`int()`  

`str()`  

#### 잠깐 멈춤 3. 아래 코드를 오류 없이 실행되도록 수정하세요  
`print("Number of letters in your name: " + len(input("Enter your name")))`