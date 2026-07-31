#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 7A

from Movie_class import Movie
from Customer_class import Customer

def main():
    movie1 = Movie("Inception", "Christopher Nolan")
    customer1 = Customer("Ethan")

    print(customer1.rent_movie(movie1))
    print(customer1.rent_movie(movie1))
    print(customer1.return_movie(movie1))
    print(customer1.return_movie(movie1))

    customer2 = Customer("Olivia")
    print(customer2.rent_movie(movie1))

    movie2 = Movie("The Matrix", "Wachowskis")
    movie3 = Movie("Interstellar", "Christopher Nolan")
    movie4 = Movie("Avatar", "James Cameron")

    print(customer1.rent_movie(movie2))
    print(customer1.rent_movie(movie3))
    print(customer1.rent_movie(movie4))

main()