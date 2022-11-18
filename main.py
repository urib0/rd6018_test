#!/usr/bin/env python3

from rd6006 import RD6006
import time
import datetime as dt

print(dt.datetime.now().strftime("%H:%M:%S.%f")[:-3])
r = RD6006("/dev/ttyUSB0")

#e = r.enable
#v = r.voltage
v = 10
a = r.current
print(f"{v},{a}")

LOOP = 10
VMIN = 1
VMAX = 20

print(f"output:{r.enable}")
#time.sleep(3)
for j in range(LOOP):
    st = dt.datetime.now()
    for i in range(VMIN,VMAX+1):
    #    print(dt.datetime.now().strftime("%H:%M:%S.%f")[:-3])
        print(f"\r{i}/{VMAX}["+"#"*i+"]",end="")
        r.voltage = i

    print(f" total time : {(dt.datetime.now()-st).total_seconds()}")

r.enable = True
print(f"output:{r.enable}")
time.sleep(10)
for j in range(LOOP):
    st = dt.datetime.now()
    for i in range(VMIN,VMAX+1):
    #    print(dt.datetime.now().strftime("%H:%M:%S.%f")[:-3])
        print(f"\r{i}/{VMAX}["+"#"*i+"]",end="")
        r.voltage = i

    print(f" total time : {(dt.datetime.now()-st).total_seconds()}")

r.enable = False
time.sleep(1)
