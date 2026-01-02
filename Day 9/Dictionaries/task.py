programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print("------------------------------------------------------------------------")

my_empty_dictionary = {}

my_empty_dictionary["minsu"] = "friends"
print(my_empty_dictionary["minsu"])

my_empty_dictionary["minsu"] = "not friends"
print(my_empty_dictionary["minsu"])
print("------------------------------------------------------------------------")

fruit = {"apple": "red", "banana": "yello", "oi": "green"}

for key in fruit:
    print(f"{key} : {fruit[key]}")
