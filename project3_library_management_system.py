import datetime as dt


class book:
    copies = 1

    genre_list = ["fantasy", "action", "young adult", "fiction", "drama", "horror", "romance",
                  "slice of life", "mystery", "non fiction", "dark fantasy", "lgbtq", "adventure"]

    def __init__(self, name, year, author, genre1=None, genre2=None, genre3=None, genre4=None, genre5=None, genre6=None):

        self.name = name
        self.year = year
        self.author = author

        self.genre1 = genre1
        self.genre2 = genre2
        self.genre3 = genre3
        self.genre4 = genre4
        self.genre5 = genre5
        self.genre6 = genre6

        book_list_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\book_list.txt'

        file1 = open(book_list_path, "r")
        content = file1.read()

        file1 = open(book_list_path, "a")
        if self.name not in content:
            a = ",{}".format(name)
            al = a.lower()
            file1.write(al)
        else:
            pass

        if self.genre1 == "fantasy" or self.genre2 == "fantasy" or self.genre3 == "fantasy" or self.genre4 == "fantasy" or self.genre5 == "fantasy" or self.genre6 == "fantasy":

            fantasy_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\fantasy.txt'
            file1 = open(fantasy_path, "r")
            content = file1.read()

            file1 = open(fantasy_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "action" or self.genre2 == "action" or self.genre3 == "action" or self.genre4 == "action" or self.genre6 == "action" or self.genre5 == "action":

            action_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\action.txt'
            file1 = open(action_path, "r")
            content = file1.read()

            file1 = open(action_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "young adult" or self.genre2 == "young adult" or self.genre3 == "young adult" or self.genre4 == "young adult" or self.genre6 == "young adult" or self.genre5 == "young adult":

            young_adult_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\young_adult.txt'
            file1 = open(young_adult_path, "r")
            content = file1.read()

            file1 = open(young_adult_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "fiction" or self.genre2 == "fiction" or self.genre3 == "fiction" or self.genre4 == "fiction" or self.genre6 == "fiction" or self.genre5 == "fiction":

            fiction_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\fiction.txt'
            file1 = open(fiction_path, "r")
            content = file1.read()

            file1 = open(fiction_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "drama" or self.genre2 == "drama" or self.genre3 == "drama" or self.genre4 == "drama" or self.genre6 == "drama" or self.genre5 == "drama":

            drama_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\drama.txt'
            file1 = open(drama_path, "r")
            content = file1.read()

            file1 = open(drama_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "horror" or self.genre2 == "horror" or self.genre3 == "horror" or self.genre4 == "horror" or self.genre6 == "horror" or self.genre5 == "horror":

            horror_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\horror.txt'
            file1 = open(horror_path, "r")
            content = file1.read()

            file1 = open(horror_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "romance" or self.genre2 == "romance" or self.genre3 == "romance" or self.genre4 == "romance" or self.genre6 == "romance" or self.genre5 == "romance":

            romance_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\romance.txt'
            file1 = open(romance_path, "r")
            content = file1.read()

            file1 = open(romance_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "slice of life" or self.genre2 == "slice of life" or self.genre3 == "slice of life" or self.genre4 == "slice of life" or self.genre6 == "slice of life" or self.genre5 == "slice of life":

            slice_of_life_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\slice_of_life.txt'
            file1 = open(slice_of_life_path, "r")
            content = file1.read()

            file1 = open(slice_of_life_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "mystery" or self.genre2 == "mystery" or self.genre3 == "mystery" or self.genre4 == "mystery" or self.genre6 == "mystery" or self.genre5 == "mystery":

            mystery_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\mystery.txt'
            file1 = open(mystery_path, "r")
            content = file1.read()

            file1 = open(mystery_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "non-fiction" or self.genre2 == "non-fiction" or self.genre3 == "non-fiction" or self.genre4 == "non-fiction" or self.genre6 == "non-fiction" or self.genre5 == "non-fiction":

            non_fiction_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\non_fiction.txt'
            file1 = open(non_fiction_path, "r")
            content = file1.read()

            file1 = open(non_fiction_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "dark fantasy" or self.genre2 == "dark fantasy" or self.genre3 == "dark fantasy" or self.genre4 == "dark fantasy" or self.genre6 == "dark fantasy" or self.genre5 == "dark fantasy":

            dark_fantasy_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\dark_fantasy.txt'
            file1 = open(dark_fantasy_path, "r")
            content = file1.read()

            file1 = open(dark_fantasy_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "lgbtq" or self.genre2 == "lgbtq" or self.genre3 == "lgbtq" or self.genre4 == "lgbtq" or self.genre6 == "lgbtq" or self.genre5 == "lgbtq":

            lgbtq_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\lgbtq.txt'
            file1 = open(lgbtq_path, "r")
            content = file1.read()

            file1 = open(lgbtq_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        if self.genre1 == "adventure" or self.genre2 == "adventure" or self.genre3 == "adventure" or self.genre4 == "adventure" or self.genre5 == "adventure" or self.genre6 == "adventure":

            adventure_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\adventure.txt'
            file1 = open(adventure_path, "r")
            content = file1.read()

            file1 = open(adventure_path, "a")
            if self.name not in content:
                a = ",{}".format(name)
                file1.write(a)
            else:
                pass

        else:
            print("You can only have upto 6 genre catagory per book make sure the genres spelling (check the genre list for correct spellings and the avaible genres) is correct and all the words are in lower case. ")

    # this code shows the info of the book.

    def book_info(self):
        return (f"the name of the book is {self.name}, the author {self.author}, written in year {self.year}, genre : {self.genre1}, {self.genre2}, {self.genre3}, {self.genre4}, {self.genre5}, {self.genre6}")

    # this code is used to borrow a book
    def borrow(self):

        book_list_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\book_list.txt'
        file1 = open(book_list_path, "r")
        content = file1.read()
        book_list = content.split(",")

        borrow_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\borrowed.txt'
        file2 = open(borrow_path, "r")
        content_borrow = file2.read()
        borrow_list = content_borrow.split(",")

        print(
            f"\nHeres a list of all the avaible in the library at the moment : {book_list}\n")

        u_book = input("Enter the name of the book you want to borrow here : ")
        ubl = u_book.lower()
        guest_name = input("\nEnter your name here : ")
        current_datetime = dt.datetime.now()
        string_date = current_datetime.strftime('%Y %m %d | %H %M %p')

        if u_book in book_list:

            print(
                "\n*************************************************************************")
            print(f"\n{ubl} has been issued by {guest_name}. ")
            book_list.remove(ubl)
            borrow_list.append(ubl)

            book_list_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\book_list.txt'
            file1 = open(book_list_path, "w")
            a = ",".join(book_list)
            file1.write(a)

            borrow_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\borrowed.txt'
            file2 = open(borrow_path, "w")
            b = ",".join(borrow_list)
            file2.write(b)

            log_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\log.txt'
            file3 = open(log_path, "a")
            file3.write(
                f"\n{u_book} was borrowed by {guest_name} on {string_date}. ")

        else:
            print(
                "\n*************************************************************************")
            print(f"\nThe book ({u_book}) is not avaible in the library or already has been issued by someone check the log file to view who has borrowed your desired book if not present in the log file the name of the book must be incorrect. ")

    # this code reutrns a book.

    def return_book(self):

        book_list_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\book_list.txt'
        file1 = open(book_list_path, "r")
        content = file1.read()
        book_list = content.split(",")

        borrow_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\borrowed.txt'
        file2 = open(borrow_path, "r")
        content_borrow = file2.read()
        borrow_list = content_borrow.split(",")

        u_book = input(
            "Enter the name of the book you want to return here (make sure the name of the book is valid) : ")
        ubl = u_book.lower()
        guest_name = input("Enter your name here : ")
        current_datetime = dt.datetime.now()
        string_date = current_datetime.strftime('%Y %m %d | %H %M %p')

        if ubl in borrow_list:

            print(
                "************************************************************************************\n")
            print("The book has been returned to the library, thank you. ")
            borrow_list.remove(ubl)
            book_list.append(ubl)

            book_list_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\book_list.txt'
            file1 = open(book_list_path, "w")
            a = ",".join(book_list)
            file1.write(a)

            borrow_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\borrowed.txt'
            file2 = open(borrow_path, "w")
            b = ",".join(borrow_list)
            file2.write(b)

            log_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\log.txt'
            file3 = open(log_path, "a")
            file3.write(
                f"\n{u_book} was returned by {guest_name} on {string_date}. ")

        else:

            print(
                "************************************************************************************\n")
            print(
                f"{u_book} was never borrowed from the library, make sure the spelling of book name is correct.")


# these are some default books:
book3 = book("aryan's smuts", "69420", "aryan", "adventure",
             "action", "dark fantasy", "mystery")
test_book = book("test", "69420", "aryan", "adventure",
                 "action", "dark fantasy", "mystery")

print("*******************************************************************************************************************************************************************************************************************\n")
print("\t\t\t\t\t\t\t\t\twelcome to murtaza's personal library management system - made by aryan")
print("\n\n*******************************************************************************************************************************************************************************************************************")

while (True):
    print("\nTHE PROGRAM IS CASE SENSITIVE AND SPACE SENITIVE SO PLEASE ENTER THE SPEELINGS AND DONT USE SPACE AFTER OR BEFORE THE BOOK NAME CORRECTLY OTHERWISE THE PROGRAM WONT RUN CORRECTLY..............\n")

    work_input = input(''' type '1' to add a new book\n type '2' to view books in the library\n type '3' to borrow a book from the library\n type '4' to return a book to the library here\n type '5' to view log file here\n type '6' to view currently borrowed books here\n type 'quit' to quit the library system: ''')

    if work_input == '1':
        uname = input("Enter the name of the book here : ")
        unl = uname.lower()
        uyear = input("Enter the year the book was published in here : ")
        uauthor = input("Enter the name of the author here : ")

        print("*******************************************************************************************************************************\n")
        print("here a list of the avaible genres please select only these genres with correct spelling and lowercase letter otherwise the program can break or give weird undisired outputs. \n")
        print(book.genre_list)
        print("\nyou can have upto 6 genres or less per book MAKE SURE THE SPELLING OF THE GENRES ARE RIGHT AND LOWERCASE. \n")
        print("if the book has less than 6 genres just type the genres that are avaible and enter 'None' in the rest genres REMEMBER THE CAPITAL 'N' in the next few genres. ")
        print("\n***********************************************************************************************************************")

        ugenre1 = input("Enter the 1st genre of the book here : ")
        ugenre2 = input(
            "Enter the 2nd genre of the book here (if the genres are over just type 'None' in the next genre lines): ")
        ugenre3 = input(
            "Enter the 3rd genre of the book here (if the genres are over just type 'None' in the next genre lines): ")
        ugenre4 = input(
            "Enter the 4th genre of the book here (if the genres are over just type 'None' in the next genre lines): ")
        ugenre5 = input(
            "Enter the 5th genre of the book here (if the genres are over just type 'None' in the next genre lines): ")
        ugenre6 = input(
            "Enter the 6th genre of the book here (if the genres are over just type 'None' in this genre lines) : ")

        ubook = book(unl, uyear, uauthor, ugenre1, ugenre2,
                     ugenre3, ugenre4, ugenre5, ugenre6)

    elif work_input == '2':

        view_input = input(
            "to view all the avaible books type 'all books', to view books of a specific genre 'genre' here : ")

        if view_input == 'all books':

            book_list_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\book_list.txt'
            file1 = open(book_list_path, "r")
            content = file1.read()
            answer = content.split(",")

            print(
                f"\nall avaible books in in the library at the moment are : \n{answer}\n")

            visual_input = input(
                "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
            if visual_input == 'yes':
                for element in range(1, len(answer)):
                    print(f"{element}. ", answer[element])

        elif view_input == "genre":
            genre_input = input(
                '''type "fantasy", "action", "young adult", "fiction", "drama", "horror", "romance", "slice of life", "mystery", "non fiction", "dark fantasy", "lgbtq", "adventure" "borrowed" for list of genre books here : ''')

            if genre_input == "fantasy":

                fantasy_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\fantasy.txt'
                file1 = open(fantasy_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall fantasy books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "action":

                action_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\action.txt'
                file1 = open(action_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall action books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "young adult":

                young_adult_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\young_adult.txt'
                file1 = open(young_adult_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall young adult books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "drama":

                drama_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\drama.txt'
                file1 = open(drama_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall drama books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "horror":

                horror_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\horror.txt'
                file1 = open(horror_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall horror books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "romance":

                romance_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\romance.txt'
                file1 = open(romance_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall romance books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "slice of life":

                slice_of_life_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\slice_of_life.txt'
                file1 = open(slice_of_life_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall slice of life books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "mystery":
                mystery_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\mystery.txt'
                file1 = open(mystery_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall mystery books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "lgbtq":
                lgbtq_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\lgbtq.txt'
                file1 = open(lgbtq_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall lgbtq books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "adventure":
                adventure_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\adventure.txt'
                file1 = open(adventure_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall adventure books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "dark fantasy":
                dark_fantasy_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\dark_fantasy.txt'
                file1 = open(dark_fantasy_path, "r")
                content = file1.read()
                answer = content.split(",")

                print(f"\nall dark fantasy books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "borrowed":

                borrow_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\borrowed.txt'
                file2 = open(borrow_path, "r")
                content_borrow = file2.read()
                borrow_list = content_borrow.split(",")

                print(f"\nall borrowed books are : \n{answer}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

            elif genre_input == "non fiction":

                non_ficiton_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\non_fiction.txt'
                file2 = open(non_ficiton_path, "r")
                non_fiction_content = file2.read()
                non_fiction_list = non_fiction_content.split(",")

                print(f"\nall non-ficiton books are : \n{non_fiction_list}\n")

                visual_input = input(
                    "\nto see all the books in a less overwhelming way type 'yes' or just press enter to continue here : ")
                if visual_input == 'yes':
                    for element in range(1, len(answer)):
                        print(f"{element}. ", answer[element])

    elif work_input == '3':
        test_book.borrow()

    elif work_input == '4':
        test_book.return_book()

    elif work_input == '5':
        log_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\log.txt'

        file = open(log_path, "r")
        content = file.read()
        print("\nthe log is as follows. note the dates are in format (year month day | hour24 min AM/PM): ")
        print(content)

        ua = input(
            "\n\nif you want to search by a perticular date, user or book type 'yes' here: ")

        if ua == "yes":
            u_search = input(
                '''\nif you want to search a perticular user's history type 'user',
if you wanna see a perticular books history type 'book', 
if you wanna see all the books that have been borrowed/returned on particular date or month or year type 'date' : ''')

            if u_search == "book":

                u_sbook = input(
                    "\n\nEnter the valid name of the book here if you are sure the book is present in the library but not visible via search, you can view the book's valid name from the library menu: ")

                line = content.split(".")
                print(
                    f"\n\nthe log with the book {u_sbook} are as follows (year month day | hour24 min AM/PM): ")
                for sentance in line:
                    logline = sentance
                    str1 = sentance.split()
                    del str1[-8:]
                    book = ""

                    for letter in str1:
                        if letter == "was":
                            break
                        else:
                            book = book + " " + letter

                    book = book[1:]
                    # print(book)
                    if book == u_sbook:
                        print(logline)

            elif u_search == "user":

                u_uname = input(
                    "Enter the name of the user who's history you wanna check here : ")
                print(
                    f"\n****the history of the user {u_uname} in format (year month day | hour24 min AM/PM) as follows: ****")
                line = content.split(".")

                for sentance in line:
                    logline = sentance
                    str1 = sentance.split()

                    del str1[-8:]

                    rev_name = ""

                    for index in range(-1, -len(str1), -1):

                        if str1[index] == "by":
                            break
                        else:
                            rev_name = rev_name + " " + str1[index]

                    stack = []

                    rev_name_list = rev_name.split()

                    if len(rev_name_list) == 1:
                        rev_name = rev_name.lstrip()

                        if rev_name == u_uname:
                            print(logline)

                    else:

                        for i in range(len(rev_name_list)):
                            stack.append(rev_name_list[i])

                        name = ""

                        for j in range(len(rev_name_list)):
                            word = stack.pop()
                            name = name + " " + str(word)

                        name = name.lstrip()

                        if name == u_uname:
                            print(logline)

            elif u_search == "date":

                # harry potter and the prisoner of azkaban was borrowed by khushi rathore on 2022 03 21 | 22 20 PM.

                ymod = input("if you wanna see books that were borrowed/returned in a perticular year type 'year',if you wanna see books that were borrowed/returned in a perticular month of a year type 'month', if you wanna see books that were borrowed/returned in a perticular day of a month of a year aka a specific date type 'date' here : ")

                if ymod == 'year':

                    u_year = input(
                        "\n\n enter the year you wanna check in which books were borrowed/returned: ")
                    print(
                        f"\n*****Here are the logs in format (year month day | hour24 min AM/PM) of year : {u_year} ****\n")
                    line = content.split(".")
                    for sentance in line:
                        str1 = sentance.split()

                        if str1 == []:
                            pass
                        else:
                            if str1[-7] == u_year:
                                print(sentance)

                elif ymod == 'month':

                    u_year = input(
                        "\n\n enter the year in which books were borrowed/returned: ")
                    u_month = input(
                        f"\n\n enter the month (in {u_year}) in which books were borrowed/returned NOTE = 'enter the single digit months in this way 03, 04, 05, 01': ")
                    print(
                        f"\n*****Here are the logs of month : {u_month} in the year : {u_year} in format (year month day | hour24 min AM/PM)****\n")
                    line = content.split(".")

                    for sentance in line:
                        str1 = sentance.split()

                        if str1 == []:
                            pass

                        else:
                            year = str1[-7]
                            month = str1[-6]

                            if u_year == year and u_month == month:
                                print(sentance)

                elif ymod == 'date':

                    u_year = input(
                        "\n\n enter the year in which books were borrowed/returned: ")
                    u_month = input(
                        f"\n\n enter the month (in {u_year}) in which books were borrowed/returned: ")
                    u_day = input(
                        f"\n\n enter the day (in month : {u_month} and year : {u_year}) in which books were borrowed/returned NOTE = 'enter the single digit days in this way '03, 04, 05, 01': ")
                    print(
                        f"\n*****Here are the logs of date : {u_year}/{u_month}/{u_day} in format (year month day | hour24 min AM/PM)****\n")
                    line = content.split(".")

                    for sentance in line:

                        str1 = sentance.split()

                        if str1 == []:
                            pass

                        else:

                            year = str1[-7]
                            month = str1[-6]
                            day = str1[-5]

                            if u_year == year and u_month == month:
                                print(sentance)

                else:
                    print(
                        "please enter a valid option  and check for spelling and caps mistakes its 'year' or 'month' or 'date'. ")

        else:
            print("\nthanks for using the library. ")

    elif work_input == "6":

        borrow_path = 'F:\\aryans_code_notes\\python_language\\murtza_library_management_system\\borrowed.txt'
        file2 = open(borrow_path, "r")
        content_borrow = file2.read()
        borrow_list = content_borrow.split(",")

        print(f"\nall borrowed books are : \n{borrow_list}\n")

    elif work_input == 'quit':
        print("\n**************************************************************************************************************\n")
        print(" Thank you for using the library system. ")
        print("\n**************************************************************************************************************\n")
        break
