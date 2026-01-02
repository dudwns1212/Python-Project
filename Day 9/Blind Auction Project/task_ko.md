목표는 블라인드 경매 프로그램을 만드는 것입니다.

### 데모
https://appbrewery.github.io/python-day9-demo/

### 출력 지우기
출력을 지우는 방법에는 여러 가지가 있습니다. 가장 쉬운 방법은 `"\n"`을 여러 번 출력하여 출력 내용이 여러 줄 아래로 스크롤되도록 하는 것입니다.

예:
```
# 출력에 20개의 새 줄을 추가합니다.
print("\n" * 20)
```

### 기능
- 각 사람은 자신의 이름과 경매 금액을 입력합니다.
- 프로그램은 다른 사람이 경매에 참여할 필요가 있는지 묻습니다. 만약 그렇다면, 컴퓨터는 출력을 지우고(여러 개의 빈 줄을 출력) 다시 이름과 경매 금액을 묻는 루프로 돌아갑니다.
- 각 사람의 이름과 경매 금액은 딕셔너리에 저장됩니다.
- 모든 참가자가 경매를 완료하면, 프로그램은 최고 입찰자를 찾아서 출력합니다.

<div class="hint">
  프로그램을 계획하기 위해 플로우차트를 작성해 보세요.
</div>

<div class="hint">
  input() 함수에서 나오는 값은 문자열(String)입니다. 이 값을 숫자로 변환하려면 int() 함수를 사용해야 합니다.
</div>

### 플로우차트

제 플로우차트를 보고 싶으시다면 [여기](https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Blind%20Auction%20Flow%20Chart#R3VnbcpswEP0aPzYDCLB5tHNrZ9pMpu6kzaMMilEDiBHyLV%2FfFYirHMdp7JD4JUGrXV3Ont2V5AE6j9fXHKfhDxaQaGAZwXqALgaWZRqmAf%2BkZFNIHM8qBHNOA6VUC6b0iZSWSrqgAclaioKxSNC0LfRZkhBftGSYc7Zqqz2wqD1riudEE0x9HOnS3zQQoZK6jl13fCV0HpZTm65X9MS41FZbyUIcsFVDhC4H6JwzJoqveH1OIoleCUxhd%2FVMb7UyThKxj8Hs4R5fx%2BMlu%2F52dxPepdM7H31BxShLHC3UjtVixaaEgASAiGoyLkI2ZwmOLmvphLNFEhA5jQGtWuc7YykITRD%2BJUJslHvxQjAQhSKOVG8xp5zo2b0pUcYW3Cc7NlSSBPM5ETv0rMoDwF3CYiL4Buw4ibCgy%2FY6sCLRvNKrYYYPhfQrUDc11Ke%2Fxj9%2FadDXwEqUViEVZJrifP8riLdtIC4JF2S9G0Z928rAHimuqmi1VXNVU99TorBBemQcCSfn1Nhp7clOu092Wjo7Q0hclhEBcDKJchbn6VWcpZsPx1mvZ84OT42z9p6cdfvkrK2hPs4e84LP4e8NjokcIUkXon%2FCOk6LsKajM9a0t1DWPhZlvVOjrLsnZUd9UtbdSdkJ2FrGLaew0Y%2FG2OpI2xtjTf0E9ckp%2B1YqKtNbRmHmynOO1fYcGnU8UoSIsuo4pVrG%2F%2FtppHM8COqEjJOgojqsQB4usLwsUl9QcESOAKwUIjmU6o9kUxnlQ54NLBfHkvDJLEsrh%2FQZKmh41gmWLQcSc%2BjoweIcLVhGfcQGWVPxR5nL7%2FuG%2FGLd6LjYlI0EdpubAISqed%2Fsq83yVml3wCg00Z6VwxweIl7HnONNQyGVcZg9H872yGxxy%2B5e%2BTv6yHN26cNHsYKDxnwFdi90Mxt0Uzw6CcI1noz6eLDQ34mKwwp9KLIzz9N5%2FpfJ5kCu141gR5MZNNy5%2FFpkhMtsvgplpl%2FhnKp51p%2FJEtBN3SGLZ4usp7RdVcqX0na3oh4Oc%2F2AeE8yDSbYtGjjgSM6T%2BDbh82DJ9BEQkN9HI1VR0yDoIg6ktEnPMuHksRW%2BQfGdSYD50KOBYGWFTF3IKiRZ7dzkmFrQG87S1pHw9nrtTxWOeo1BbKVrerk9Q75arhnvnrrC9b2gmZ1HnvQcL%2Fz7GsLbbdwOvbuQttd12v1zeE7FGZTf5o6jwjm1fk68zkhiZ6I3%2FkMjZzOK%2FSWVLztSe9ot80y9TSAu6L5LaTALYQ1kEyUdQyuMlVX%2ByqT2wTEj4pKCSpx%2B4azokkii2fPHnCGL3vA9LYUQ%2FdoLrA0F9ywT18LXdTB2dBxRoephdCsf2osMkr9iy26%2FAc%3D#%7B%22pageId%22%3A%22fezw1VAINj_9lBO2EaiH%22%7D)를 다운로드하여 확인할 수 있습니다.