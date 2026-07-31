#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 10B

class Dog:
    def __init__(self, age, weight, name, fur_color, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.fur_color = fur_color
        self.breed = breed

    def bark(self):
        print(" Woof! Woof!")

    def rename(self, new_name):
        self.name = new_name

    def eat(self, food_weight):
        self.weight += food_weight

    def __str__(self):
        return f" {self.name} is a {self.age} year old {self.fur_color} {self.breed} that weighs {self.weight} lbs."

print("You are about to create a dog.")
age = int(input(" How old is the dog: "))
weight = float(input(" How much does the dog weigh: "))
name = input(" What is the dog's name: ")
fur_color = input(" What color is the dog: ")
breed = input(" What breed is the dog: ")

dog = Dog(age, weight, name, fur_color, breed)
print(dog)
dog.bark()

food_amount = float(input(f" {dog.name} is hungry, how much should he eat: "))
new_name = input(f" {dog.name} isn't a very good name. What should they be renamed to: ")

dog.eat(food_amount)
dog.rename(new_name)

print(dog)