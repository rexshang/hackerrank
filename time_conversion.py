'''
Created on Nov 7, 2016

@author: erexsha
'''
import sys


time = raw_input().strip()
r = time.split(':')

hour = int(r[0])
minute = int(r[1])
second = int(r[2][:2])
ampm = r[2][2:4]

if ampm == "PM":
    if hour < 12:
        hour = hour + 12
elif ampm == "AM":
    if hour >= 12:
        hour = hour - 12
else:
    print "error"
    
#print minute
#print ampm
m_time = [hour, minute, second]

print '{:02d}:{:02d}:{:02d}'.format(*m_time)