# Reading the first line
# Using a with fucntion to define a text file as a variable, seperate out the first line and print it

with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
print(first_line)