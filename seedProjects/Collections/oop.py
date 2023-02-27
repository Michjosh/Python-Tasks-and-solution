class Human:
    name = "Michael"
    age = 16

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __set_name__(self, firstname):
        self.name = firstname

    def get_name(self):
        return self.name


employee = Human("Jessa", 20)
print(employee.name, employee.age)

if __name__ == "__main__":
    print(employee.name, employee.age)
