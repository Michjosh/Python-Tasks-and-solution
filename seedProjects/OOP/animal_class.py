class Animal:

    # def _init_(self): ...

    def _init_(self, name, speak, dance, run):
        self.animal_name = name
        self.animal_speech = speak
        self.animal_dance_skill = dance
        self.animal_run = run
        self.animal_list = []

    def set_animal_name(self, name):
        self.animal_name = name

    def get_name(self):
        return self.animal_name

    def set_animal_speech(self, speak):
        self.animal_speech = speak

    def get_speech(self):
        return self.animal_speech

    def set_animal_dance_skill(self, dance):
        self.animal_dance_skill = dance

    def get_dance_skill(self):
        return self.animal_dance_skill

    def set_animal_run(self, run):
        self.animal_run = run

    def get_run(self):
        return self.animal_run

    def set_animal_list(self, *values):
        # for i in range(len(values)):
        #    self.animal_list.append(values[i])
        # self.animal_list = [values[i] for i in range(len(values))]
        self.animal_list = [i for i in values]

    def get_animal_list(self):
        return self.animal_list

    def get_animal_list_size(self):
        return len(self.animal_list)

