import zipfile
import os
from logger import logger


def unzip_tmp_file(file_name, tmp_dir):
    '''
    Unzip files to temp dir, add list of files to xml_file_list, remove .zip file
    :param file_name:
    :param tmp_dir:
    :return: _xml_file_list
    '''
    _zip_file = zipfile.ZipFile(file_name, 'r')
    _files_list = _zip_file.namelist()
    _xml_file_list = []
    for _xmlfile in _files_list:
        if '.xml' in _xmlfile:
            _xml_file_list.append(_xmlfile)
            _zip_file.extract(_xmlfile, tmp_dir)
            logger(f'{_xmlfile}', '_xml_file_list')
    _zip_file.close
    os.remove(file_name)
    logger(f'{file_name} unziped and removed', 'unzip')
    return _xml_file_list

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

