class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f"{self.name} is {self.age} years old"


philo = Dog("Philo", 5, "brown")

print(Dog.__str__(philo))

