#!/usr/bin/env python3
import sys
from serial import Serial
from datetime import datetime
from collections import OrderedDict

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("Please specify a device.\n")
        sys.exit(-1)

    now = datetime.now()
    ds1307 = OrderedDict()
    ds1307['seconds'] = now.second // 10 << 4 | now.second % 10
    ds1307['minutes'] = now.minute // 10 << 4 | now.minute % 10
    ds1307['hours'] = now.hour // 10 << 4 | now.hour % 10
    ds1307['day'] = now.isoweekday()
    ds1307['date'] = now.day // 10 << 4 | now.day % 10
    ds1307['month'] = now.month // 10 << 4 | now.month % 10
    ds1307['year'] = now.year % 100 // 10 << 4 | now.year % 1000

    with Serial(sys.argv[1], 9600) as s:
        s.write(bytes([0xFA]))
        for i, value in enumerate(ds1307.values()):
            s.write(bytes([0x10 | i]))
            s.write(bytes([0x20 | value >> 4 & 0x0F]))
            s.write(bytes([0x30 | value & 0x0F]))
        s.write(bytes([0x60]))
