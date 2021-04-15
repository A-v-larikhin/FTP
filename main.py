import os
from ftp_func_s import ftp_connect, get_ftp_file, ftp_con_close
from zip_file import unzip_tmp_file
from xml_file import xml_parsing
from logger import logger
from db_func_s import connect_to_db, db_insert

# List of zip files on ftp-server
txt_file = './txt/Sankt-Peterburg-notifications.txt'    # in folder:/fcs_regions/Sankt-Peterburg/notifications/

# Temp directory to unzip .xml files
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

# Make DataBase and FTP connections:
con = connect_to_db()
ftp = ftp_connect()

# Do magic:
for list in file_list:
    file = get_ftp_file(list, ftp)
    xml_file_list = unzip_tmp_file(file, tmp_dir)
    for xml_file in xml_file_list:
        try:
            print(f'try: {xml_file}')
            not_id, not_purch_num, not_href, not_price = xml_parsing(tmp_dir + xml_file)
            #db_insert(con, not_id, not_purch_num, not_href, not_price)
            logger(f'success; {list[0]}', 'xml_to_db')
        except:
            logger(f'error; {list[0]}', 'xml_to_db')
            break
    break

# Close connections:
ftp_con_close(ftp)
con.close()
