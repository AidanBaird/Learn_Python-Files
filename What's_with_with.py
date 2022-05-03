# Correcting un optimal code

# close_this_file = open('fun_file.txt')

with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)
