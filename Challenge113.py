# ----------*CHALLENGE 113*----------* 
# Using the Books.csv file, ask the user how many records
# they want to add to the list and then allow them to add
# that many. After all the data has been added, ask for an
# author and display all the books in the list by that author.
# If there are no books by that author in the list, display a
# suitable message.

import csv

number_records = int(input("How many records you have in the list Books?: "))

file = open("Books.csv","a")

for addBooks in range (0,number_records):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the release year of publication: ")

    newRecord = ("\n"+title+","+author+","+year)
    file.write(str(newRecord))
    
file.close()

search = input("What author do you wanna display their books: ")

file = open("Books.csv","r")
reader = csv.reader(file)
is_search = True
if is_search == True:
    for row in file:
        if search in str(row):
            print(row)
        else:
            is_search = False
if is_search == False:
    print("The enter data is incorrect or the author is not in our data bases. Try again.")