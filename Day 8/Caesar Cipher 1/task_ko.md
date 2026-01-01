당신은 [카이사르 암호](https://en.wikipedia.org/wiki/Caesar_cipher)를 사용하여 암호화 및 복호화 프로그램을 만들 것입니다.

### 데모
https://appbrewery.github.io/python-day8-demo/

### TODO-1:  
`encrypt()`라는 이름의 함수를 생성하세요. 이 함수는 `original_text`와 `shift_amount`라는 2개의 입력값을 받습니다.

### TODO-2:  
`encrypt` 함수 내부에서, `original_text`의 각 문자를 `shift_amount`만큼 알파벳에서 앞으로 이동시키고, 암호화된 텍스트를 출력하세요.

Python의 내장 함수 `index()`를 사용하여 리스트에서 항목의 위치를 찾을 수 있습니다. 예:
```
fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear") #1
```

예를 들어 다음과 같은 값이 주어졌다면:
```
plain_text = "hello"
shift_amount = 1
```
최종 암호화된 출력값은 아래와 같이 나와야 합니다:

`여기 암호화된 결과가 있습니다: ifmmp`

'hello'의 각 문자가 1만큼 위로 이동했습니다.  

<div class="hint">
문제를 분해해봅시다:

1. plain_text 안의 각 문자를 순회하기 위해 for 루프가 필요합니다.  
2. 알파벳 리스트에서 각 문자의 위치를 찾습니다.  
3. 사용자가 지정한 shift_amount를 위치 값에 더해서 암호화된 문자의 위치를 구합니다.  
4. 그 위치에 해당하는 문자를 찾습니다.  
5. 루프가 끝난 후, 모든 암호화된 문자를 새로운 문자열에 추가하고 출력하세요.  
</div>

### TODO-3:  
`encrypt()` 함수를 호출하고 사용자 입력값을 전달하세요. 코드를 테스트하고 메시지를 암호화할 수 있어야 합니다.

### TODO-4:  
문자 'z'를 9만큼 앞으로 이동시키려고 하면 어떻게 될까요? 코드를 수정할 수 있나요?

<div class="hint">
이 문제를 해결할 수 있는 다양한 접근법이 있습니다.
1. 알파벳 문자의 리스트에 알파벳 세트를 여러 번 추가할 수 있습니다.  
2. shift_amount를 0에서 25 사이의 값으로 조정하여 리스트에 맞게 만들 수 있습니다.  
3. 나머지를 구하기 위해 모듈로(modulo)를 사용할 수 있습니다.  
</div>