import re

class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        print("updating user email address from: {email} to: {address}".format(email=self.email, address=address))
        self.email = address
        

    def __repr__(self):
        return "User {user}, email: {email}, books read: {books}".format(user=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if other_user.name == self.name and other_user.email == self.email:
            return True
        else:
            return False
    
    def read_book(self,book, rating = "None"):
        self.books[book] = rating
        
    def get_average_rating(self):
        total = 0
        for rating in self.books.values():
            if isinstance(rating, int):
                total += rating
        return total / len(self.books)

    
    
class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        print("updating ISBN for book title {title} from: {isbn} to: {new_isbn}".format(title=self.title, isbn=self.isbn, new_isbn=new_isbn))
        self.isbn = new_isbn
           
    def add_rating(self, rating):
        
        if rating == "None" or (rating >= 0 and rating <= 4):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return false
              
    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            if isinstance(rating, int):
                total += rating
        return total / len(self.ratings)
    
    def __hash__(self):
        return hash((self.title, self.isbn))

            
        
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author
        
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)
            
            
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        self.available_books = {}

    def __repr__(self):
        return "TomeRater: {users}".format(users=self.users, books=self.books)

        
    def check_isbn_unique(self, isbn):
        for book in self.available_books:
            if book.get_isbn() == isbn:
                print("ISBN {isbn} is already added".format(isbn=isbn))
    
    def create_book(self, title, isbn):
        self.check_isbn_unique(isbn)
        new_book = Book(title, isbn)
        self.available_books[new_book] = isbn
        return new_book
    
    def create_novel(self, title, author, isbn):
        self.check_isbn_unique(isbn)
        new_novel = Fiction(title, author, isbn)
        self.available_books[new_novel] = isbn
        return new_novel
    
    def create_non_fiction(self, title, subject, level, isbn):
        self.check_isbn_unique(isbn)
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        self.available_books[new_non_fiction] = isbn
        return new_non_fiction
    
    
    def check_email_not_exist(self, email):
        if email in self.users:
            print("User already exists with email address {email}!".format(email=email))
    
    def check_email_valid(self, email):
        valid_email = re.search("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.(com|edu|org)$", email)
        if not valid_email:
            print("Email address {email} is invalid".format(email=email))
    
    def add_book_to_user(self, book, email, rating = "None"):  

        if email in self.users:
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            
            if book in self.books:
                self.books[book] +=1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}!".format(email=email))
    
    def add_user(self, name, email, user_books = "None"):
        self.check_email_valid(email)
        self.check_email_not_exist(email)
        new_user = User(name, email)

        new_user_hash = {email: new_user}
        self.users.update(new_user_hash)
        if user_books != "None":
            for user_book in user_books:
                self.add_book_to_user(user_book, email)
    
    
    
    def print_catalog(self):
        for book in self.books:
            print("Title: {title}, ISBN: {isbn}".format(title=book.get_title(), isbn=book.get_isbn()))
    
    def print_users(self):
        for user in self.users.values():
            print(user)
    
   
    def most_read_book(self):
        most_books = 0
        most_read_book = ""
        for book, count in self.books.items():
            if count > most_books:
                most_books = count
                most_read_book = book
        return most_read_book
                
            
    def highest_rated_book(self):
        highest_rating = 0
        higest_rated_book = ""
        for book in self.books:
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                higest_rated_book = book
        return higest_rated_book
                    
    def most_positive_user(self):
        max_rating = 0
        most_positive_user = ""
        for user in self.users.values():
            if user.get_average_rating() > max_rating:

                max_rating = user.get_average_rating()
                most_positive_user = user
        return most_positive_user
                    
    
                
    
