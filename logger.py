def logger(line, filename):
    with open(f'./log/{filename}.log', 'a') as log_f:
        log_f.write(line + '\n')
    log_f.close()
