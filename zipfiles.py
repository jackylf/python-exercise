import zipfile

my_zipfile = zipfile.ZipFile('..\\new\\new2.zip')
zipped_files = my_zipfile.namelist()
print(zipped_files)
file_info = my_zipfile.getinfo('new2/chap 13/read_word_doc.py')
print(zipped_files[21])
print(file_info.file_size)
print(file_info.compress_size)

my_zipfile.close()