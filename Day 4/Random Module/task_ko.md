### 의사난수 생성기
컴퓨터는 회로와 스위치로 구성되어 있어 완전한 랜덤을 생성할 수 없습니다. 그러나 특히 게임을 작성할 때 랜덤성은 매우 중요합니다. 만약 비디오 게임에서 모든 움직임이 미리 결정되어 있다면, 정말 지루할 것입니다.

그래서 일부 컴퓨터 과학자들은 의사난수 생성기(Pseudorandom Number Generators)를 발명했습니다. 예: https://en.wikipedia.org/wiki/Mersenne_Twister

의사난수 생성기에 대해 더 배우고 싶다면, Khan Academy의 이 비디오를 추천합니다: https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs

### Python의 Random 모듈
다음을 통해 문서를 읽어보세요:
https://docs.python.org/3/library/random.html

사용하려면 먼저 모듈을 가져와야 합니다:

`import random`

### 범위 내 랜덤 정수

```
import random
rand_num = random.randint(1, 10)

# 이것은 1과 10 사이의 랜덤 정수를 생성합니다(둘 다 포함).
```

### Python의 모듈
Python은 코드를 서로 다른 파일로 나누어 필요 시 가져올 수 있습니다. 이를 통해 코드를 더 잘 정리하고 모듈화할 수 있습니다.

새로운 `.py` 파일을 생성하여 새로운 모듈을 만들 수 있으며, `import` 키워드를 사용해 해당 파일의 변수나 함수를 가져올 수 있습니다.

### 랜덤 부동소수점 수
random 모듈에서 다음 코드를 사용하여 0.0(포함)에서 1.0(미포함) 사이의 랜덤 숫자를 생성할 수 있습니다:

```
import random
rand_num_0_to_1 = random.random()
```
다음과 같이 표현될 수 있습니다:

`0.0 <= random.random() < 1.0`

이 방식을 사용하면 곱셈을 통해 랜덤 숫자의 범위를 확장할 수 있습니다.

예: `random.random() * 5`

위 코드는 0과 5 사이의 랜덤 숫자를 생성합니다.

또 다른 방법으로는 `uniform()` 함수를 사용하는 것입니다.

```
import random
random_float = random.uniform(1, 10)
# 이것은 1과 10 사이의 랜덤 부동소수점 숫자를 생성합니다.
```
이 방법은 부동소수점 숫자의 반올림에 따라 상한값이 포함될 수도, 포함되지 않을 수도 있습니다.
따라서 다음과 같이 표현하는 것이 가장 적절합니다:

`a <= random.uniform(a,b) <= b`

상한값 포함 여부에 따라 `random.random()` 또는 `random.uniform()` 중 어떤 것을 사용할지 선택해야 합니다.

### PAUSE 1 - 앞면 또는 뒷면
Python의 랜덤화에 대해 배운 내용을 사용하여 동전 던지기 프로그램을 만들어 보세요. 이 프로그램은 실행될 때마다 "앞면" 또는 "뒷면"을 랜덤하게 출력해야 합니다.

<div class="hint">
  Python의 조건문에 대해 배운 내용을 생각해보세요.
</div>