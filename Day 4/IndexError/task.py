states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america) # 그냥 리스트를 모두 출력
print(len(states_of_america)) # 리스트의 길이(개수)
print(len(states_of_america[0])) # 0번째 index 원소의 길이

# 그럼 index 범위를 벗어난 숫자를 입력하면?
#print(states_of_america[50])  -> IndexError 발생

# 중첩리스트, 2차원 리스트
mount_food = ['beef', 'namul']
sea_food = ['fish', 'solt']
food = [mount_food, sea_food]
print(food)
