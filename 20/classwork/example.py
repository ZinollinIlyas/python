from datetime import datetime


class Log:
    def __init__(self):
        self.entries = []

    def write(self, text):
        self.entries.append(text)

    def read(self):
        for text in self.entries:
            print(text)


class TimeLog(Log):
    def write(self, text):
        self.entries.append(f"{datetime.now()}")
        super().write(text)
