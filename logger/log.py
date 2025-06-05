from datetime import datetime
import sys

def log(abc):
    time = datetime.now()
    sys.stderr.write(time.strftime("[%Y.%m.%d %H:%M:%S]"))
    sys.stderr.write(f"{abc}")

log('123123')