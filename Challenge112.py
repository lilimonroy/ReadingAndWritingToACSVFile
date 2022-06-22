# ----------*CHALLENGE 112*----------* 
# Using the Books.csv file from program 111, ask the user to enter another record and add it to the end of the file. 
# Display each row of the .csv file on a separate line.

import csv

file = open("Books.csv","a")
title = input("Enter the title of the book: ")
author = input("Enter the author's name: ")
year = input("Enter the year released: ") 

newRecord = "\n"+title+","+author+","+year

file.write(str(newRecord))
file.close()

file = open("Books.csv","r")
for row in file:
    print(row)
file.close()