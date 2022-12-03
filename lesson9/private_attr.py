import pprint


class Car:
    def __init__(self, manufacturer: str, model: str, color: str,
                 fuel_consumption: float, fuel_tank_capacity: float):
        self.manufacturer: str = manufacturer
        self.model: str = model
        self.color: str = color
        self.fuel_consumption = fuel_consumption
        self.fuel_tank_capacity = fuel_tank_capacity
        self.__km: int = 0
        self.fuel: float = 0

    def __str__(self):
        return f"{self.manufacturer} | Model: {self.model} | Year: {self.year}"


    def fill_tank(self, amnt: float) -> bool:
        if amnt <= 0:
            return False
        if amnt + self.fuel > self.fuel_tank_capacity:
            return False

        self.fuel += amnt
        return True

    def drive(self, kms_driven: int):
        if (self.fuel_consumption / 100) * kms_driven <= self.fuel:
            self.__km += kms_driven
            self.fuel -= (self.fuel_consumption / 100) * kms_driven
            return True
        else:
            return False


if __name__ == '__main__':
    car_mazda: Car = Car('Mazda', '3', 'white', 20, 60)
    car_toyota = Car('Toyota', 'Yaris', 'red', 25, 45)
    print(car_toyota.__dir__())