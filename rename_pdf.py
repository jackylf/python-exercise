import os,re,shutil

#construct the Regex to find file names ends with '(year)'
fileNameRegex = re.compile(r'''(\d{1,2}\.)  #number
                            (.*?)           #all text after num and before '(year)'
                            (\s\(\d{4}\))   #'(year)'
                            (\.pdf)         #file suffix
                            ''',re.VERBOSE)
#TODO: loop through all the files and change those files where their names match Regex
filePath = r'I:\\____技术阅读\\1. 数据分析\\3. Python'
files = os.listdir(filePath)
for file in sorted(files):
    mo = fileNameRegex.search(file)
    if mo:
        print(f'{mo.group()}')
        print(f'{mo.group(1)}{mo.group(3)}{mo.group(2)}{mo.group(4)}')
        old_name = filePath + '\\' + file
        new_name = filePath + '\\' + f'{mo.group(1)}{mo.group(3)}{mo.group(2)}{mo.group(4)}'
        shutil.move(old_name, new_name)
