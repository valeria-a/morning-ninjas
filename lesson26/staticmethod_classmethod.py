class BestFruit:

    green_fruits = ('Apple', 'Pear', 'lime')
    tropical_fruits = ('Passionfruit', 'Mangustin')

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def get_name(self):
        return self._name

    @staticmethod
    def get_tropical():
        return Fruit.tropical_fruits

    @classmethod
    def get_green_fruits(cls):
        return cls.green_fruits


if __name__ == '__main__':
    print(Fruit.get_tropical())
    print(Fruit.get_green_fruits())