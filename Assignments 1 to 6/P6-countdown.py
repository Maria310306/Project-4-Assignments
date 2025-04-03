import time 

def count_down(t):
    while t:
        min, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end="\r")
        time.sleep(1)
        t -=1

    print('Time finished!')
t= int(input('Enter the time in seconds: '))
count_down(int(t))    
