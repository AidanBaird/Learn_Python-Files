# Introduction to "Readlines()"
# Open a text file and use a for loop to print each individual line

with open("how_many_lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)