# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)

bgp = {}
type_no = True

name_list = []
bid_list = []

while type_no:
    name = input("What is your name?:\t")
    bid = int(input("What is your bid?:\t$"))
    types = input("Are there any other bidders? Type 'yes' or 'no'.")

    name_list.append(name)
    bid_list.append(bid)


    if types != 'yes':
        type_no = False
    else:
        print("\n" * 20)
bgp = {
    "name" : name_list,
    "bid" : bid_list
}

print(bgp) ## name과 bid를 가지는 리스트 형태의 dictionary 생성
maxi = 0
name = ''

for index,big in enumerate(bgp["bid"]):
    if big > maxi:
        maxi = big
        name = bgp["name"][index]
    bgp["winner"] = [name, maxi]

print(f"The winner is {bgp["winner"][0]} with a bid of ${bgp['winner'][1]}")