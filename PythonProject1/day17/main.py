class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
        print(f"user_id : {id}, user_name : {name}, user_followers : {self.followers}, user_following : {self.following}")

    def follow(self, user):
        user.followers += 1
        self.following += 1

# 클래스를 활용해 객체를 만듦
user_1 = User("001", "angela" )

user_2 = User("002", "jack")

user_1.follow(user_2)
print(f"user_1의 followers : {user_1.followers}, user_2의 followers : {user_2.followers}\n"
      f"user_1의 following : {user_1.following}, user_2의 following : {user_2.following}")