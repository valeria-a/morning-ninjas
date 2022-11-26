my_car = {
    'manufacturer': 'Mazda',
    'model': '3',
    'color': 'white',
    'license_plate': '1234567',
    'year': 2015,
    'fuel': 50,
    'km': 102000,
    'fuel_consumption': 20
}

def add_fuel(car, liters):
    car['fuel'] += liters

def drive(car, km):
    car['km'] += km

# what should we do if we also want to update info about fuel left?



# We want something like (pseudocode - will not run!):

# Create an object, it has internal state
# car = Car(manufacturer='Mazda', model='3', fuel=50,...)

# "Use" the object bu applying actions on it - and internal state will change accordingly
# (increas km), add/reduce fuel, etc...
# car.add_fuel(liters=20)
# car.drive(km=200)
# car.get_fuel_left()
# car.is_out_of_fuel()
# ...

# Cars “remember” things about their current state
# Cars functions (methods) that can change that state
# We can manage each car separately