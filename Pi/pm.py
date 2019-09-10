
import time
from pms5003 import PMS5003, ReadTimeoutError

print("""particulates.py - Print readings from the PMS5003 particulate sensor.
Press Ctrl+C to exit!
""")

pms5003 = PMS5003()
time.sleep(1.0)

try:
    while True:
        try:
            readings = pms5003.read()
            print(readings)
            time.sleep(60)
        except ReadTimeoutError:
            pms5003 = PMS5003()
except KeyboardInterrupt:
    pass

