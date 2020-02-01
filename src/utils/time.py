from datetime import datetime

class LogDate(object):
    _now = datetime.now()

    def Year(self):        
        return f'{str(self._now.day)}/{str(self._now.month)}/{str(self._now.year)}'

    def Hour(self):
        return f'{str(self._now.hour)}/{str(self._now.minute)}/{str(self._now.second)}'
    
