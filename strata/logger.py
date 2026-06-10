from datetime import datetime

class Logger:
    LEVELS = ("INFO", "WARN", "ERROR")
    
    def log(self, level, message):
        if level not in self.LEVELS:
            raise ValueError(f"Invalid log level: {level}")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {level:<5} {message}")
    
    def info(self, message):
        self.log("INFO", message)
        
    def warn(self, message):
        self.log("WARN", message)
        
    def warn(self, message):
        self.log("WARN", message)