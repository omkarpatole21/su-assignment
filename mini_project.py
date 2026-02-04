class Person:
    def __init__(self, id, name):
        self._id = id
        self._name = name


class Car:
    def __init__(self, car_id, brand, model, year):
        self._car_id = car_id
        self._brand = brand
        self._model = model
        self._year = year
        self._is_available = True

    def rent_car(self):
        self._is_available = False

    def return_car(self):
        self._is_available = True

    def is_available(self):
        return self._is_available

    def display(self):
        if self._is_available:
            print(f"{self._brand} {self._model} is Available")
        else:
            print(f"{self._brand} {self._model} is Rented")

class Customer(Person):
    def __init__(self, customer_id, name):
        super().__init__(customer_id, name)
        self._rented_cars = []

    def rent(self, car):
        self._rented_cars.append(car)

    def return_car(self, car):
        self._rented_cars.remove(car)

    def show_rented_cars(self):
        print("\nCars rented by", self._name)
        if len(self._rented_cars) == 0:
            print("No cars rented")
        else:
            for car in self._rented_cars:
                car.display()


class CarRentalSystem:
    def __init__(self):
        self._cars = []
        self._customers = []

    def add_car(self, car):
        self._cars.append(car)
        print("Car added successfully")

    def add_customer(self, customer):
        self._customers.append(customer)
        print("Customer added successfully")

    def rent_car(self, car, customer):
        if car.is_available():
            car.rent_car()
            customer.rent(car)
            print("Car rented successfully")
        else:
            print("Car is not available")

    def return_car(self, car, customer):
        car.return_car()
        customer.return_car(car)
        print("Car returned successfully")

    def show_available_cars(self):
        print("\nAvailable Cars:")
        for car in self._cars:
            if car.is_available():
                car.display()

s = CarRentalSystem()


n = int(input("Enter number of cars: "))
for i in range(n):
    car_id = int(input("Enter car id: "))
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))
    s.add_car(Car(car_id, brand, model, year))


m = int(input("\nEnter number of customers: "))
for i in range(m):
    cust_id = int(input("Enter customer id: "))
    name = input("Enter customer name: ")
    s.add_customer(Customer(cust_id, name))


while True:
    print("\n1. Show Available Cars")
    print("2. Rent Car")
    print("3. Return Car")
    print("4. Show Customer Rented Cars")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        s.show_available_cars()

    elif choice == 2:
        car_id = int(input("Enter car Id: "))
        cust_id = int(input("Enter customer Id: "))
        s.rent_car(s._cars[car_id], s._customers[cust_id])

    elif choice == 3:
        car_id = int(input("Enter car Id: "))
        cust_id = int(input("Enter customer Id: "))
        s.return_car(s._cars[car_id], s._customers[cust_id])

    elif choice == 4:
        cust_id = int(input("Enter customer Id: "))
        s._customers[cust_id].show_rented_cars()

    elif choice == 5:
        break

    else:
        print("Invalid choice")