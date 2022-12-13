from datetime import datetime
from time import sleep

from settings import LOG_FILE

def print_title(msg, width = 40, sleep_time = 0.3):
    print('-' * width)
    print(msg.center(width))
    print('-' * width)
    sleep(sleep_time)
    
    
def print_body(*msgs, width = 40, sleep_time = 1):
    for msg in msgs:
        print(msg)
    print('-' * width)
    sleep(sleep_time)
    print()


def log_register(msg):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f'{time_now} - {msg}'
        
        print(msg)
        f.write(f'{msg}\n')
        
          