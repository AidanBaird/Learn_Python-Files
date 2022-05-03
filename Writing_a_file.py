# Writing a new file with code
# Creating a .txt file out side of the script for later use

with open("bad_actors.txt", "w") as bad_actors_doc:
  bad_actors_doc.write("Jared Leto")
  