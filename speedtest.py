import subprocess,time,os

datafile='speeddata.csv'
try: os.remove(datafile)
except: pass

my_timeout=60
p = subprocess.Popen(['./startrinity_cst/CST.CrossPlatform', '--download-limit', '125', '--upload-limit', '0', '--output-measurements', datafile])
time.sleep(my_timeout)
p.kill()


speed=[]
for i,line in enumerate(file(datafile)):
    if i>0:
        line=line.split(',')
        speed.append(float(line[2].split('Mbps/')[0]))
speed=sum(speed)/len(speed)

import gspread
from datetime import datetime

dt=datetime.now()
dt = dt.strftime("%Y-%m-%d %H:%M")

gc = gspread.service_account()
sh = gc.open("Logging")
sh.sheet1.append_row([dt, speed], value_input_option='USER_ENTERED')

