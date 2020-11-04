class Library():
    def __init__(self,listofbooks,libraryname):
        self.lb=listofbooks
        self.ln=libraryname
        self.dictionary = {}
    def displaybook(self):
        print("Index --- Book Name")
        for index,names in enumerate(self.lb):
            print(index,"    ---",names)
        # print(f"Books Name : {self.lb}")
    def lendbook(self,bookname):
        if bookname not in self.lb:
            print("This book is not in the library")
        elif bookname in self.dictionary:
            print(f"This book is lend by {self.dictionary[bookname]} ")
        elif bookname in self.lb:
            username=input("Please enter your name: ")
            self.dictionary[bookname]=username
            print("Thank for coming!!!")
    def addbook(self,addbook):
        if addbook in self.lb:
            print("Book already present in the library")
        else:
            self.lb.append(addbook)
            print("Book added in the library successfully")
    def returnbook(self,return_book):
        if return_book in self.dictionary:
            self.dictionary.pop(return_book)
            print("Thank you for returning the book.Please do visit again")
        else:
            print("Enter valid book name")

Comicbooks=["Brainmaster","Captain Atom","Cyberswine","Cyclone","Dark Nebula","Dee Vee","The Example","Fire Fang","Greener Pastures"]
Australia=Library(Comicbooks,"Australia Comic books")

def main():
    print("\nPress 1.Display Book\n"
          "Press 2.Lend Book\n"
          "Press 3.Add Book\n"
          "Press 4.Return Book\n"
          "Press 5.Exit")
    user =input("Enter the number: ")
    try:
        userinput=int(user)
        while True:
            if userinput == 1:
                Australia.displaybook()
                main()
            elif userinput == 2:
                lend_book_name=input("Select the book from Display list and enter the book name: ")
                Australia.lendbook(lend_book_name)
                main()
            elif userinput == 3:
                add_book_name=input("Enter the book name to add: ")
                Australia.addbook(add_book_name)
                main()
            elif userinput == 4:
                return_book_name=input("Enter the book name to be returned: ")
                Australia.returnbook(return_book_name)
                main()
            elif userinput == 5:
                break
            else:
                print("Enter Proper input")
                main()
    except:
        print("Enter only the given number for the Library methods")
        main()
main()
