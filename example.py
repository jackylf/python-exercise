import openpyxl
import pprint
import datetime as dt

wb =  openpyxl.load_workbook('example.xlsx')
sht = wb.worksheets[0]

# allData = {date: [(fruit, quantity)]}
# fruit有重复，所以不能使用dictionary
allData = {}
records = []
for row_num in range(1, sht.max_row+1):
    date = sht['A'+ str(row_num)].value.strftime("%d/%m/%Y %H:%M")
    fruit = sht['B'+ str(row_num)].value
    quantity = sht['C'+ str(row_num)].value

    records.append((fruit,quantity))
    allData[date] = records[row_num-1]

with open('example.txt', 'w') as file_obj:
    file_obj.write('allData = ' + pprint.pformat(allData))
