class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner}'s account : ${self.balance}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
        

class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name}'s salary is {self.salary} in company {self.company}"
        
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'Woof')

    # def speak(self):
    #     return "Woof"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'Meow')

    # def speak(self):
    #     return "Meow"

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

class Vehicle:
    def __init__(self):
        pass

    def describe(self):
        return "Vehicle class is the super class"

class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def describe(self):
        return f"Car class is the sub class of {super().describe()}"

class ElectricCar(Car):
    def __init__(self):
        super().__init__()

    def describe(self):
        return f"Electric Car class is the sub class of {super().describe()}"
    
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, title):
        self.songs.append(title)

    def remove_song(self, title):
        if title in self.songs:
            self.songs.remove(title)
        else:
            print(f"{title} not found in the playlist")

    def __str__(self):
        return "\n".join(self.songs)

@dataclass
class Student:
    name : str
    scores : list

    def average(self):
        return  sum(self.scores) / len(self.scores)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

def main():
    # account = BankAccount("Ritik")
    # print(account)
    # account.deposit(10)
    # print(account)
    # account.withdraw(20)
    # print(account)
    # account.withdraw(10)
    # print(account)

    # e1 = Employee("Ritik", 10000)
    # e2 = Employee("Neha", 20000)
    # print(e1)
    # print(e2)

    # d = Dog("Doggo")
    # c = Cat("cattie")
    # print(d.speak())
    # print(c.speak())

    # print(Point(1, 2) == Point(1,2))

    # c = ElectricCar()
    # print(c.describe())

    # p = Playlist('Indian')
    # p.add_song('First')
    # p.add_song('Second')
    # p.add_song('Third')
    # p.add_song('Fourth')
    # print(p)
    # p.remove_song('First')
    # print(p)


if __name__ == "__main__":
    main()