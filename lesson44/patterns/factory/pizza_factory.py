from abc import ABC, abstractmethod

import textfiles

# The Factory design pattern is a popular design pattern because
# it provides a way to create objects without specifying their exact class.
# This decouples the creation of objects from their use, making the code more flexible and easier to maintain.
class Pizza(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Margherita(Pizza):
    def get_name(self):
        return "Margherita"

    def get_price(self):
        return 5.0


class Pepperoni(Pizza):
    def get_name(self):
        return "Pepperoni"

    def get_price(self):
        return 7.0


class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == "Margherita":
            return Margherita()
        elif pizza_type == "Pepperoni":
            return Pepperoni()
        else:
            raise ValueError("Invalid pizza type")
