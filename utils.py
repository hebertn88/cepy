from datetime import datetime
from time import sleep


def print_title(msg, width = 40, sleep_time = 0.5):
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
    
'''
class TimeControl:
    def __init__(self):
        self.time = self.get_time_now()
        self.hour = self.time.hour
        self.minute = self.time.minute
        self.second = self.time.second
        
    def __repr__(self):
        return(f'Time = {self.time}')
        
    def set_time(self, time):
        self.time = time
        self.hour = time.hour
        self.minute = time.minute
        self.second = time.second

    def get_time_now():
        return datetime.now()
'''