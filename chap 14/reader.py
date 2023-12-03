import csv,os

file_path = os.path.join(os.getcwd(),'chap 14','example.csv')
with open(file_path, newline='') as my_file:
    reader = csv.reader(my_file)
    print(reader)