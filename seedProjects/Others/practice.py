class Guitar:
    def __init__(self):
        self.n_strings = 6
        self.play()

    def play(self):
        print("pam pam pam pam")


# my_guitar = Guitar()


class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__()
        self.n_strings = 8
        self.colour =("00000", "75483")
        self.__cost = 50

    def playLouder(self):
        print("pam pam pam pam".upper())

    def __secret(self):
        print("This guitar actually cost a lot", self._ElectricGuitar__cost, )
        my_new_guitar.playLouder()


my_new_guitar = ElectricGuitar()

my_new_guitar._ElectricGuitar__secret()

#
# print("Child class:", my_new_guitar.n_strings)
# print("Parent class:", Guitar().n_strings)

# print(my_new_guitar._ElectricGuitar__cost)


