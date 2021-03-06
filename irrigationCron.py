from serial import Serial
from subprocess import check_output
from time import sleep
from re import findall

device = findall('ttyUSB[0-9]*', check_output(["ls","/dev"]))[0]
s = Serial('/dev/' + device, 9600)

sleep(5)

command='valve_on'
s.write(command.encode())
status = s.readline().decode('ascii').strip()

sleep(10)

command='valve_off'
s.write(command.encode())
status = s.readline().decode('ascii').strip()
