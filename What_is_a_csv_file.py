# Example of how to open and read a .csv file

with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())