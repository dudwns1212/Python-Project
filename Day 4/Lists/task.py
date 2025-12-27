phone = ["Samsung", "Apple", "Shalom", "LG"]
        #    0         1        2        3
        #   -4        -3       -2       -1
print(phone[0])
print(phone[1])
print(phone[2])
print(phone[3])
print("--------------------------------")
phone[0] = "ICON"  # 이렇게 다른 값을 넣어 항목을 수정할 수 있음
print(phone[0]) # ICON
print(phone[1]) # Apple
print("--------------------------------")
# 항목 추가 => append
phone.append("Samsung")
print(phone[4]) # 마지막 인덱스에 추가