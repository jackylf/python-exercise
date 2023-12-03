import os

for folderName, subfolders, fileNames in os.walk('..\\new'):
    print(f'The current folder is {folderName}')

    for subfolder in subfolders:
        print(f'    Subfolders are: {subfolder}')
    
    for filename in fileNames:
        print(f'    files are: {filename}')
    