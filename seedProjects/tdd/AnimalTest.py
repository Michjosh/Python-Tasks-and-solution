import unittest

from seedProjects.OOP.animal_class import Animal


class TestAnimalClass(unittest.TestCase):
    animal = Animal()

    def test_animal_name(self):
        # given
        self.animal.set_animal_name("Snoopy")
        # when
        result = self.animal.get_name()
        # assert
        self.assertEqual("Snoopy", result)

    def test_animal_speech(self):
        # given
        self.animal.set_animal_speech("bark")
        # when
        language = self.animal.get_speech()
        # assert
        self.assertEqual("bark", language)

    def test_animal_dance_skill(self):
        # given
        self.animal.set_animal_dance_skill("wiggle")
        # when
        dance = self.animal.get_dance_skill()
        # assert
        self.assertEqual("wiggle", dance)

    def test_animal_run(self):
        # given
        self.animal.set_animal_run("150 m/hr")
        # when
        miles = self.animal.get_run()
        # assert
        self.assertTrue("150 m/hr", miles)

    def test_that_a_list_exist(self):
        self.animal.set_animal_list(1, 3, 3, 4, 5)
        size = self.animal.get_animal_list()
        self.assertIsNotNone(size)

    def test_length_of_list(self):
        self.animal.set_animal_list(1, 3, 3, 4, 5)
        size = self.animal.get_animal_list_size()
        print(self.animal.animal_list)
        self.assertEqual(5, size)