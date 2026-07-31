#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 7A Movie_class

class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            return "You rented the movie"
        return "Movie already rented"

    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
            return "You returned the movie"
        return "Movie is not rented"