# exercise 1
def count_vowels(text):
    if not isinstance(text, str):
        return 42
    count = 0
    vowels = set("aeiouAEIOU")
    for i in text:
        if i in vowels:
            count = count + 1
    return count


print(count_vowels("Hello"))
print(count_vowels("ELLIE"))
print(count_vowels(1998))


# exercise 2
def hamming(text1, text2):
    if len(text1) != len(text2):
        return 0
    hamming_distance = 0
    for i in range(0, len(text1)):
        if text1[i] != text2[i]:
            hamming_distance = hamming_distance + 1
    return hamming_distance


print(hamming("cat", "kat"))
print(hamming("horse", "cat"))
print(hamming("horse", "apple"))



# exercise 3
class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        # only works for python 3+
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Doors: {2}".format(self.color, self.fuel_type, self.doors)


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        # only works for python 3+
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Passengers: {2}".format(self.color, self.fuel_type, self.passengers)

car1 = Car("Blue","Diesel", 2)
bus1 = Bus("Red", "Benzin", 40)

print(car1)
print(bus1)



# exercise 4
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return "{0}, {1}".format(self.name, self.author)

book1 = Book("Dune", "Frank Herbert")
print(book1)



# exercise 5
class BookShelf:
    books = []

    def add_book_list(self, books):
        for book in books:
            if isinstance(book, Book):
                self.books.append(book)

    def books_by_author(self, author):
        list_books = []
        for book in self.books:
            if book.author == author:
                list_books.append(book.name)
        return list_books

    def get_books(self):
        list_all_books = []
        for book in self.books:
            list_all_books.append(book.name)
        return list_all_books

    def clear_shelf(self):
        self.books = []

book2 = Book("Moby Dick", "Herman Melville")
book3 = Book("Robinson Crusoe", "Daniel Defoe")
book4 = Book("Robinson Crusoe the Sequel", "Daniel Defoe")
book_list = {book1, book2, book3, book4}

shelf = BookShelf()
shelf.add_book_list(book_list)

print(shelf.get_books())
print(shelf.books_by_author("Daniel Defoe"))

shelf.clear_shelf()
print(shelf.get_books())
