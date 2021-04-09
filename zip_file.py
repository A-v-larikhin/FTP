import zipfile

zip_file = zipfile.ZipFile('./tmp/notification_Sankt-Peterburg_2014010100_2014020100_122.xml.zip', 'r')
files_list = zip_file.namelist()
xml_file_list = []
tmpdir = './tmp/tmpdir/'

for file in files_list:
    if '.xml' in file:
        print(file)
        xml_file_list.append(file)
        zip_file.extract(file, tmpdir)

# zip_file.extractall('./tmp/dir1')
zip_file.close

