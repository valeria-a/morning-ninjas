# Implementing the Animal classes
from textfiles.csv_file import CsvFile
from textfiles.file_factory import TextFile
from textfiles.json_file import JsonFile


# Subject
class Animal:
    def speak(self):
        pass


# Concrete Subjects
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Fish(Animal):
    def speak(self):
        return "Blub!"

# Implementing the Factory Method
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        elif animal_type.lower() == "fish":
            return Fish()
        else:
            return None



if __name__ == '__main__':
    TextFile.make_file_instance("csv")
    CsvFile("gsjhdf")