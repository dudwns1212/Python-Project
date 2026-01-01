### TODO-1:  
`decrypt()`라는 이름의 함수를 생성하고, 이 함수는 `original_text`와 `shift_amount`를 두 가지 입력으로 받습니다.

### TODO-2:  
`decrypt()` 함수 내에서 `original_text`의 각 문자를 알파벳에서 *뒤로* `shift_amount`만큼 이동시키고, 복호화된 텍스트를 출력하세요.

<div class="hint">
  어떤 숫자라도 -1을 곱하면 음수로 만들 수 있습니다.
</div>

### TODO-3:  
- `encrypt()`와 `decrypt()` 함수를 결합하여 `caesar()`라는 단일 함수로 만드세요.  
- 사용자가 선택한 `direction` 변수 값을 사용해 어떤 기능을 실행할지 결정하세요.  
- `encrypt`/`decrypt` 대신 `caesar` 함수를 호출하고 세 가지 변수인 `direction`/`text`/`shift`를 전달하세요.

<div class="hint">
  숫자에 -1을 곱했을 때 부호가 반전된다는 것을 기억하세요.  
예: <code>3 + (5 * -1)</code>는 <code>3 - 5</code>와 동일합니다.
</div>

<div class="hint">
결과 메시지는 다음과 같이 표시되어야 합니다:  

<code>Here is the encoded result: XXX</code>  

또는  

<code>Here is the decoded result: XXX</code>  
</div>