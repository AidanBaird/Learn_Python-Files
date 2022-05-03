# Introduction to "with" functions
# Opening a file then turning it into a variable and printing it

with open("welcome.txt") as text_file:
  text_data = text_file.read()
print(text_data)