당신의 목표는 Python 프로그래밍에서 배운 모든 것을 사용하여 [행맨 게임](https://en.wikipedia.org/wiki/Hangman_(game))을 만드는 것입니다.

### 데모 최종 프로젝트
https://appbrewery.github.io/python-day7-demo/

이 프로젝트는 5개의 주요 단계로 나뉩니다. 각 단계에서 여러 가지 TODO 작업이 주어질 것입니다. 목표는 각 TODO 작업을 순서대로 진행하며 완료하는 것입니다.

PyCharm에서 View -> Tool Windows -> TODOs로 이동하여 모든 TODO 작업을 쉽게 확인할 수 있습니다.

### TODO-1  
`word_list`에서 무작위로 단어를 선택하여 `chosen_word`라는 변수에 할당하십시오. 그런 다음 이를 출력하세요.

### TODO-2  
사용자에게 글자를 추측하게 한 뒤 답변을 `guess`라는 변수에 할당하세요. `guess`에 저장된 문자열을 소문자로 변환하세요.

<div class="hint">
  Python에서 `lower()` 함수에 대해 Google에서 검색해 보세요.
</div>

### TODO-3  
사용자가 추측한 글자 `guess`가 `chosen_word`의 글자 중 하나인지 확인하세요. `chosen_word`의 각 글자를 반복하여 검사하고, 글자가 일치하면 "Right"를, 그렇지 않으면 "Wrong"을 출력하세요.

<div class="hint">
  문자열을 반복하는 방법은 리스트를 반복하는 방법과 동일합니다 - `for in` 루프를 사용하면 됩니다.  
  Google에서 "Loop through strings python"을 검색해 보세요.
</div>