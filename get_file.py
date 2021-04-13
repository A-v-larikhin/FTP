import ftplib

def get_ftp_file(file_list):
    ftp = ftplib.FTP('ftp.zakupki.gov.ru')
    ftp.login('free', 'free')
    try:
        with open(file_list[1], 'wb') as local_file:
            ftp.retrbinary('RETR ' + file_list[0], local_file.write)
    except ftplib.error_perm:
        with open ('./log/log.txt', 'a') as log_f:
            log_f.write(file_list[0])
        log_f.close()
        pass
    ftp.quit()
    return file_list[1]
