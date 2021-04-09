import ftplib
import sys


ftp = ftplib.FTP('ftp.zakupki.gov.ru')
ftp.login('free', 'free')
list = ftp.nlst('/fcs_regions/Sankt-Peterburg/notifications')
f = open('Sankt-Peterburg-notifications.txt', 'w')
for i in list:
    f.write(i+'\n')
    print(i)
f.close()

ftp.quit()
#ftp.cwd('/fcs_regions/')
#lines = []
#ftp.retrlines('LIST', lines.append)

#sys.stderr = open('1.txt', 'w')
#f = open('fcs_regions.txt', 'a')
#f.write(data)
#f.close()
#print(type(data))
