import openpyxl, os

file_path = os.path.join(os.getcwd(),'chap 12','example.xlsx')
wb = openpyxl.load_workbook(file_path)
my_sheet = wb['Sheet1']
