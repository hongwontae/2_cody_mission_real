import random

print(random.random())
print(random.randint(1,10))

print(random.randrange(1,10))

test = ["test", "mm"]

print(random.choice(test))

test2 = [1,2,3,4,5,6,7,8,9,10]
print(random.choices(test2, k=5))

test3 = [1,5,10,15,20]
print(random.sample(test3, len(test3)))
random.shuffle(test3)
print(test3)