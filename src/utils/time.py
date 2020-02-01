from datetime import datetime

class LogDate(object):
    _now = datetime.now()

    def Year(self):        
        return f'{str(self.now.day)}/{str(self.now.month)}/{str(self.now.year)}'

    def Hour(self):
        return f'{str(self.now.hour)}/{str(self.now.minute)}/{str(self.now.second)}'
    
