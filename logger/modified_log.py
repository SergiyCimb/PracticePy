from datetime import datetime
import sys

class Logger:
    def __init__(self, stream, time_format):
        self.stream = stream
        self.time_format = time_format

    def log(self, message):
        timestamp = datetime.now().strftime(self.time_format)
        self.stream.write(f"[{timestamp}] {message}")
        
out_stream = sys.stderr
time_formatter = '%Y-%m-%d %H:%M:%S'
logger = Logger(out_stream, time_formatter)
logger.log('message for logging')