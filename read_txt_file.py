import os
from get_file import get_ftp_file
from zip_file import unzip_tmp_file
from xml_file import xml_parsing

txt_file = './txt/Sankt-Peterburg-notifications.txt'
tmp_dir = './tmpxml/notification/'
if not os.path.isdir(tmp_dir):
    os.mkdir(tmp_dir)

# Make list [[ftp_file_name, local_filename], [ftp_file_name, local_filename]]
file_list = []
f = open(txt_file,'r')
for line in f:
    tmp_list = []
    line = line.rstrip('\n')
    if '.xml' in line:
        tmp_list.append(line)
        tmp_list.append(tmp_dir + line.split('/')[-1])
        file_list.append(tmp_list)

for list in file_list:
    file = get_ftp_file(list)
    xml_file_list = unzip_tmp_file(file, tmp_dir)
    for xml_file in xml_file_list:
        xml_parsing(tmp_dir + xml_file)
    break