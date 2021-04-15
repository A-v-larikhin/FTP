import ftplib
from logger import logger


def ftp_connect():
    '''
    Make FTP connection
    :return: FTP connection
    '''
    try:
        ftp = ftplib.FTP('ftp.zakupki.gov.ru')
        ftp.login('free', 'free')
        logger(f'ftp connected', 'ftp')
    except ftplib.error_perm as err_message:
        logger(f"can't connect; {err_message}", 'ftp')
    return ftp


def get_ftp_file(file_list, ftp):
    '''
    Try to get file from FTP and log it
    :param file_list: [ftp_file, local_file]
    :param ftp: FTP connection
    :return: local file name
    '''
    try:
        with open(file_list[1], 'wb') as local_file:
            ftp.retrbinary('RETR ' + file_list[0], local_file.write)
        local_file.close()
        logger(f'success; {file_list[0]}', 'ftp')
    except ftplib.error_perm as err_message:
        logger(f'{err_message}; {file_list[0]}', 'ftp')
    return file_list[1]


def ftp_con_close(ftp):
    try:
        ftp.quit()
        logger(f'ftp connection closed', 'ftp')
    except ftplib.error_perm as err_message:
        logger(f"can't close ftp connection; {err_message}", 'ftp')
