import zipfile
import os

def unzip_tmp_file(file, tmp_dir):
    zip_file = zipfile.ZipFile(file, 'r')
    print(file)
    files_list = zip_file.namelist()
    xml_file_list = []
    for xmlfile in files_list:
        if '.xml' in xmlfile:
            print(xmlfile)
            xml_file_list.append(xmlfile)
            zip_file.extract(xmlfile, tmp_dir)
    zip_file.close
    print(file)
    os.remove(file)
    return xml_file_list

if __name__ == '__main__':
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

