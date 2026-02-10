# # #FileNotFound
# # with open("a_file.txt") as file:
# #     file.read()
# #
# # #KeyError
# # a_dictionary = {"key":"value"}
# # value = a_dictionary["non_existent_key"]
# #
# # #IndexError
# # fruit_list = ['apple', 'bananan', 'orange']
# # fruit = fruit_list[3]
# #
# # #TypeError
# # my_snak = "Jelly"
# # print(my_snak + 5)
#
# try:
#     file = open("a_file.txt")
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("Chihiro")
# except KeyError:
#     print("That key does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     print("이건 꼭 해야돼")
#     raise KeyError("This is my Error, I made it")
#

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meter")

bmi = weight / height ** 2
print(bmi)