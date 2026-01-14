from turtle import Turtle, Screen
# 다른 파일의 클래스를 import하여 내 클래스에서 객체를 생성할 수 있음
timy = Turtle()
print(timy)
timy.shape("turtle")
timy.color("red")
timy.forward(100)

my_screen = Screen()
print(my_screen.canvwidth)

# 생성한 객체를 활용해 메소드를 실행할 수 있음
my_screen.exitonclick()

# 라이브러리에 있는 다양한 메서드를 활용할 수 있음
