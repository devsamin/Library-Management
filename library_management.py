class Book:
    def __init__(self,id,name,catagori,quantity):
        self.id = id
        self.name = name
        self.catagori= catagori
        self.quantity = quantity
class User:
    def __init__(self, user_id, user_name, password):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.borrowedbooks = []
class Library:
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        self.books = []
        self.users = []
        self.returnbooks = []
    
    def addbook(self,id,name,catagori,quantity):
        book = Book(id,name,catagori,quantity)
        self.books.append(book)
        print(f"\n\t{name} Book Added successfully  !")
    
    def adduser(self,user_id, user_name, password):
        user = User(user_id, user_name, password)
        self.users.append(user)
        return user
    
    def borrowbook(self,user,book_id):
        for book in self.books:
            if book.id == book_id:
                if book.quantity > 1:
                    if book in user.borrowedbooks:
                        print("\n\t Already Borrowed  !")
                        return
                    else:
                        user.borrowedbooks.append(book)
                        book.quantity -= 1
                        print(f"\n\t{book.name} Borrowed successfully  !")
                        return
                else:
                    print("\n No availabale copes")
                    return
            
        print(f"\n\tNot Found  !")

    def returnbook(self, user_id, book_id):
        for book in user_id.borrowedbooks:
            if book.id == book_id:
                pi.returnbooks.append(book)
                user_id.borrowedbooks.remove(book)
                book.quantity+=1
                print(f"\n\t{book.name} Returned successfully !")
                return
        print(f"\n\tBook not found in borrowed books !")


# class instance or object
pi = Library('samin', 'programming traning')
pybook = pi.addbook(100,'python','a',7)
admin = pi.adduser(11,'admin',123)
samin = pi.adduser(12,'samin',111)
# pi.borrowbook(admin, 100)
# pi.borrowbook(admin, 100)

# flag = True
curr_user = admin
while True:
    
    if curr_user is None:
        print("\n\tNo loggin in User")
        option = (input("Logging or Register (L/R) --> "))
        if option == 'R':
            id = int(input("\tEnter id :"))
            name = (input("\tEnter your name :"))
            password = int(input("\tEnter your password :"))
            user = pi.adduser(id,name,password)
            curr_user = user
            print(f"\n\t{curr_user.user_name} Register Successfully !")
        elif option == 'L':
            id = int(input("\tEnter id :"))
            password = int(input("\tEnter your password :"))

            same = False
            for user in pi.users:
                if id == user.user_id and password == user.password:
                    curr_user = user
                    same = True
                    print(f"\n\t{curr_user.user_name} Loging Successfully !")
                    break
            if same == False:
                print("\t No user found  !")
    else:
        if curr_user.user_name == 'admin':
            print("\t<-------------WELCOME------------->\n")
            print("<--------------ADMIN PROPARTY--------------->\n")
            print("Choice Option :\n")
            print("1. Add Book")
            print("2. Show all Book")
            print("3. Show all User")
            print("4. Logout")

            Choice = int(input("\n\tEnter Option : "))
            if Choice == 1:
                id = int(input("\tEnter id :"))
                name = input("\tEnter name : ")
                catagori = input("\tEnter catagori : ")
                quantity = int(input("\tEnter quantity : "))

                pi.addbook(id,name,catagori,quantity)
            elif Choice == 2:
                for book in pi.books:
                    print(f"Book id :{book.id}, Book Name :{book.name}, Quantity : {book.quantity}")
            elif Choice == 3:
                for user in pi.users:
                    print(f"User id :{user.user_id}, User Name :{user.user_name}")
            elif Choice == 4:
                curr_user = None
                print("Logout is successfully  !")
            else:
                print("Invalid user Existing  !")
                break
        else:
            print("\t<-------------WELCOME------------->\n")
            print("\t<--------------USER PROPARTY--------------->\n")
            print(f"User Name : {curr_user.user_name}\n")
            print("Choice Option :\n")
            print()
            print("1. Borrowed Book")
            print("2. Return Book")
            print("3. Show Book")
            print("4. Show Borrow Book")
            print("5. Show Return Book")
            print("6. Logout")

            Choice = int(input("\n\tEnter Option :"))
            if Choice == 1:
                Book_id = int(input("\n\tEnter Book Id :"))
                pi.borrowbook(curr_user,Book_id)
            elif Choice == 2:
                id = int(input("\n\tEnter Book id :"))
                pi.returnbook(curr_user,id)
            elif Choice == 3:
                for book in pi.books:
                    print(f"Book id :{book.id}, Book Name :{book.name}, Quantity : {book.quantity}")
            elif Choice == 4:
                for book in curr_user.borrowedbooks:
                    print(f"Book id :{book.id},Book Name :{book.name}")
            elif Choice == 5:
                if pi.returnbooks:
                    for book in pi.returnbooks:
                        print(f"Book id :{book.id},Book Name :{book.name}")
                else:
                    print("No books have been returned")
            elif Choice == 6:
                curr_user = None
                print("Logout successfully !")
            else:
                print("Invalid Option !")