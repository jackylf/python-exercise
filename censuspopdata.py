import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.worksheets[0]

counts = {}
# counts = {state: {county: {'census':0, 'pop':0}}}

for row_num in range(2, sheet.max_row+1):
    state = sheet['b' + str(row_num)].value
    county = sheet['c' + str(row_num)].value
    pop = sheet['d' + str(row_num)].value

    counts.setdefault(state, {})
    counts[state].setdefault(county, {'census':0, 'pop':0})

    counts[state][county]['census'] += 1
    counts[state][county]['pop'] += int(pop)

with open('censuspopdata2.py', 'w') as file_obj:
    file_obj.write('counts = ' + pprint.pformat(counts))


