import os, csv

os.makedirs(name='header_removed', exist_ok=True)

for csvfile in os.listdir('.\\removeCsvHeader'):
    if not csvfile.endswith('.csv'):
        continue
    # read all the rows in the csvfile but the first row
    print('Removing header from ' + csvfile + '...')
    
    file_path = os.path.join(os.getcwd(), 'removeCsvHeader', csvfile)
    file_obj = open(file_path, 'r')
    csv_reader = csv.reader(file_obj)
    rows = []
    for row in csv_reader:
        if csv_reader.line_num == 1:
            continue
        rows.append(row)
    # write the contents in the new csv files
    file_path = os.path.join(os.getcwd(), 'header_removed', csvfile)
    file_obj = open(file_path, 'w', newline='')
    csv_writer = csv.writer(file_obj)
    for row in rows:
        csv_writer.writerow(row)
    file_obj.close()
