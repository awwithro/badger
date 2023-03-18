import badger2040
import badger_os
import gc
import os
import sys

DETAILS_FONT_SIZE=0.5
X_OFF=10
Y_OFF=15

badger = badger2040.Badger2040()

alloc = gc.mem_alloc()
free = gc.mem_free()
uname = os.uname()
disk = badger_os.get_disk_usage()
used = disk[0]/disk[1]

badger.pen(0)
text = [
    "{}".format(uname.version),
    "Name: {}".format(uname.nodename),
    "Machine: {}".format(uname.machine),
    "Mem: {} / {}".format(alloc,free),
    "Disk: {} / {}".format(used, disk[0]),
    "Python: {}".format(sys.version),
    ]
for y, txt in enumerate(text, 1):
    badger.text(txt, X_OFF, Y_OFF * y, DETAILS_FONT_SIZE) 

badger.update()

while True:
    badger.halt()
