import sys
import time
import itertools
import logging
import re
from globals import G

def logging_init(logger, loglevel):

    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % loglevel)

    logger.setLevel(level=numeric_level)

    fmt = logging.Formatter(G.simple_fmt)

    console = logging.StreamHandler()
    console.setFormatter(fmt)
    logger.addHandler(console)

    return logger


def conv_unit(s):
    " convert a unit to number"
    d = { "B": 1,
         "K": 1024,
         "M": 1024*1024,
         "G": 1024*1024*1024,
         "T": 1024*1024*1024*1024}
    s = s.upper()
    match = re.match(r"(\d+)(\w+)", s, re.I)
    if match:
        items = match.groups()
        v = int(items[0])
        u = items[1]
        return v * d[u]

    return False

def bytes_fmt(n):
    d = {'1mb': 1048576,
         '1gb': 1073741824,
         '1tb': 1099511627776}
    if n < d['1mb']:
        return "%.2f KiB" % (float(n)/1024)

    if n < d['1gb']:
        return "%.2f MiB" % (float(n)/d['1mb'])

    if n < d['1tb']:
        return "%.2f GiB" % (float(n)/d['1gb'])

    return "%.2f TiB" % (float(n)/d['1tb'])


# SO: http://stackoverflow.com/questions/13520622/python-script-to-show-progress
def spiner():
    for c in itertools.cycle('|/-\\'):
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.2)

# SO: http://stackoverflow.com/questions/3002085/python-to-print-out-status-bar-and-percentage

def progress():
    import sys
    total = 10000000
    point = total / 100
    increment = total / 20
    for i in xrange(total):
        if(i % (5 * point) == 0):
            sys.stdout.write("\r[" + "=" * (i / increment) +  " " * ((total - i)/ increment) + "]" +  str(i / point) + "%")
            sys.stdout.flush()

