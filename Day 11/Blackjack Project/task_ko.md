### 난이도를 선택하세요
- **보통** 😎: 아래의 모든 힌트를 사용하여 프로젝트를 완성하세요.
- **어려움** 🤔: 힌트 1, 2, 3만 사용하여 프로젝트를 완성하세요.
- **매우 어려움** 😭: 힌트 1, 2만 사용하여 프로젝트를 완성하세요.
- **전문가** 🤯: 힌트 1만 사용하여 프로젝트를 완성하세요.

### 블랙잭 게임 하우스 규칙

- 카드 덱의 크기는 무제한입니다.
- 조커 카드는 사용하지 않습니다.
- Jack/Queen/King은 모두 10으로 계산됩니다.
- Ace는 11 또는 1로 계산될 수 있습니다.
- 다음 리스트를 카드 덱으로 사용하세요:

`cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- 리스트의 카드들은 동일한 확률로 선택됩니다.
- 뽑힌 카드는 덱에서 제거되지 않습니다.
- 컴퓨터가 딜러 역할을 합니다.

<div class="hint" title="Hint 1">
  아래 웹사이트에 접속하여 블랙잭 게임을 해보세요: 

https://games.washingtonpost.com/games/blackjack/

그런 다음 완성된 블랙잭 프로젝트를 여기에서 확인해보세요: 

https://appbrewery.github.io/python-day11-demo/
</div>

<div class="hint" title="Hint 2">
프로그램 요구사항에 대한 분석을 읽어보세요: 

http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

그런 다음 프로그램의 흐름도를 직접 작성해보세요.
</div>

<div class="hint" title="Hint 3">
제가 만든 이 흐름도를 다운로드하고 읽어보세요:

https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
</div>

<div class="hint" title="Hint 4">
아래 리스트를 사용하여 랜덤 카드를 반환하는 <code>deal_card()</code> 함수를 만드세요.

<code>cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]</code>

11은 Ace를 의미합니다.
</div>

<div class="hint" title="Hint 5">
<code>deal_card()</code>와 <code>append()</code>를 사용하여 사용자와 컴퓨터에게 각각 2장의 카드를 나눠주세요.

<code>user_cards = []</code>

<code>computer_cards = []</code>
</div>

<div class="hint" title="Hint 6">
리스트 형태의 카드를 입력으로 받아 리스트에 있는 모든 카드의 합계를 점수로 반환하는 <code>calculate_score()</code> 함수를 만드세요. 이를 위해 Python의 <code>sum()</code> 함수에 대해 구글링해보세요.
</div>

<div class="hint" title="Hint 7">
<code>calculate_score()</code> 안에서 블랙잭(카드 두 장: Ace + 10)을 확인하고 실제 점수 대신 <code>0</code>을 반환하세요. <code>0</code>은 게임에서 블랙잭을 나타냅니다.
</div>

<div class="hint" title="Hint 8">
<code>calculate_score()</code> 안에서 11(Ace)을 확인하세요. 점수가 이미 21을 초과했다면 11을 제거하고 1로 대체하세요. Python 내장 함수 <code>append()</code>와 <code>remove()</code>에 대한 문서를 찾아보세요.

https://developers.google.com/edu/python/lists#list-methods
</div>

<div class="hint" title="Hint 9">
<code>calculate_score()</code>를 호출하세요. 컴퓨터나 사용자가 블랙잭(0)을 가지고 있거나 사용자의 점수가 21을 초과한 경우 게임이 종료됩니다.
</div>

<div class="hint" title="Hint 10">
게임이 종료되지 않았다면, 사용자가 카드를 한 장 더 뽑을 것인지 물어보세요. 네라고 하면 <code>deal_card()</code> 함수를 사용하여 <code>user_cards</code> 리스트에 카드를 추가하세요. 아니오라고 하면 게임이 종료됩니다.
</div>

<div class="hint" title="Hint 11">
새로운 카드가 뽑힐 때마다 점수를 다시 확인해야 하며, Hint 9의 조건들을 게임이 끝날 때까지 반복해야 합니다.
</div>

<div class="hint" title="Hint 12">
사용자의 턴이 끝나면 컴퓨터가 플레이할 차례입니다. 컴퓨터는 점수가 17 미만일 동안 계속 카드를 뽑아야 합니다.
</div>

<div class="hint" title="Hint 13">
<code>compare()</code>라는 함수를 생성하고, <code>user_score</code>와 <code>computer_score</code>를 전달하세요.  

- 컴퓨터와 사용자의 점수가 같다면 비깁니다.
- 컴퓨터가 블랙잭(0)을 가지고 있다면 사용자가 집니다.
- 사용자가 블랙잭(0)을 가지고 있다면 사용자가 이깁니다.
- <code>user_score</code>가 21을 초과하면 사용자가 집니다.
- <code>computer_score</code>가 21을 초과하면 컴퓨터가 집니다.
- 위의 조건에 해당하지 않는 경우, 점수가 더 높은 플레이어가 승리합니다.
</div>

<div class="hint" title="Hint 14">
사용자에게 게임을 다시 시작할 것인지 묻습니다. 만약 그렇다면 콘솔을 초기화하고 새로운 블랙잭 게임을 시작하며 art.py의 로고를 표시하세요.
</div>