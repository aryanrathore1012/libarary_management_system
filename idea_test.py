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

        u_sbook = input("\n\nEnter the valid name of the book here if you are sure the book is present in the library but not visible via search, you can view the book's valid name from the library menu: ")

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

        ymod = input(
            '''if you wanna see books that were borrowed/returned in a perticular year type 'year',
if you wanna see books that were borrowed/returned in a perticular month of a year type 'month'
if you wanna see books that were borrowed/returned in a perticular day of a month of a year aka a specific date type 'date' here : ''')

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
            print("please enter a valid option  and check for spelling and caps mistakes its 'year' or 'month' or 'date'. ")

else:
    print("\nthanks for using the library. ")
