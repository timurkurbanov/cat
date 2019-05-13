class Cat:
    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return "My name is {} and I eat {} at {}". format(self.name, self.preferred_food, self.meal_time)

    def eats_at(self):
        if self.meal_time >= 24:
            return None
        elif 23 <= self.meal_time >= 12:
            return "{} PM".format(self.meal_time)
        else:
            return "{} AM".format(self.meal_time)

    def meow(self):
        return "My name is {} and I eat {} at {}". format(self.name, self.preferred_food, self.meal_time)

cat1 = Cat('Rocky', 'fish', 11)
cat2 = Cat('Balbo', 'meat', 17)
cat3 = Cat('Lucky', 'rise', 20)


print(cat1.meow())
print(cat2.meow())
print(cat3.meow())

