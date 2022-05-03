#

import csv

with open("books.csv") as books_csv:
  book_reader = csv.DictReader(books_csv, delimiter= "@")
  isbn_list = [book['ISBN'] for book in book_reader]
  print(isbn_list)
  #for book in book_reader:
    #print(book["ISBN"])