
#!/usr/bin/python

import sys
import serial
import time

# init serial, open arduino to check the port that the arduino is using
ser = serial.Serial('/dev/ttyACM1')

# let the arduino rest
time.sleep(1.5)

# write stuff to it!
ser.write('boom')
ser.close()
