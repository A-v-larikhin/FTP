import ftplib
import sys


ftp = ftplib.FTP('ftp.zakupki.gov.ru')
ftp.login('free', 'free')

out_file = './tmp/notification_Sankt-Peterburg_2014010100_2014020100_122.xml.zip'
ftp_filename = '/fcs_regions/Sankt-Peterburg/notifications/notification_Sankt-Peterburg_2014010100_2014020100_122.xml.zip'

try:
    with open(out_file, 'wb') as local_file:
        ftp.retrbinary('RETR ' + ftp_filename, local_file.write)
except ftplib.error_perm:
    pass

ftp.quit()