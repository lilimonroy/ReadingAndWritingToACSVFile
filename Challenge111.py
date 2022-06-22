# ----------*CHALLENGE 111*----------* 
# Create a .csv file that will store the following data. Call it “Books.csv”:
# |    |        Book                                |    Author              |   Year Released
# |  0 | To Kill A Mockingbird                      | Harper Lee             |      1960
# |  1 | A Brief History of Time                    | Stephen Hawking        |      1988
# |  2 | The Great Gatsby                           | F. Scott Fitzgerald    |      1922
# |  3 | The Man Who Mistook His Wife for a Hat     | Oliver Sacks           |      1985
# |  4 | Pride and Prejudice                        | Jane Austen            |      1813

import csv

file = open("Books.csv", "w")
newRecord = "To Kill A Mockingbird,Harper Lee,1960\nA Brief History of Time,Stephen Hawking,1988\nThe Great Gatsby,F. Scott Fitzgerald,1922\nThe Man Who Mistook His Wife for a Hat,Oliver Sacks,1985\nPride and Prejudice,Jane Austen,1813"
file.write(str(newRecord))
file.close()
