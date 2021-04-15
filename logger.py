from datetime import datetime


def logger(line, filename):
    '''
    Add some info to log file in ./log dir
    :param line: Data to log
    :param filename: Logfile name in ./log dir
    :return:
    '''
    with open(f'./log/{filename}.log', 'a') as log_f:
        log_f.write(f'{datetime.now()}; {line}\n')
    log_f.close()
