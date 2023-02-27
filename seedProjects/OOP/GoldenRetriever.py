from seedProjects.OOP.Dog_class import Dog


class GoldenRetriever(Dog):

    def speak(self, sound):
        return f"{self.name} says {sound}"


gd = GoldenRetriever("bingo", 4, "blue")

print(gd.speak("Back"))