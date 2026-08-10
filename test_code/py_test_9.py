class Car :

    share_value_speed = 100

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def speed_change (self, sp) :
        self.speed = sp;

    def color_change (self, col) :
        self.color = col

car1 = Car(200, "Red");
car2 = Car(300, "Blue");

print(car1.speed)
print(car1.color)
print(car2.speed)
print(car2.color)




