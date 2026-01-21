class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

key = [1,2,3,4,5,6,7,8,9]
print(key[::2])