class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        if not isinstance(self.year, int):
            raise DateTimeError("year", self.year, "an integer")
        elif self.year < 0 or self.year > 9999:
            raise DateTimeError("year", self.year, "between 0 and 9999")
        elif not isinstance(self.month, int):
            raise DateTimeError("month", self.month, "an integer")
        elif self.month < 1 or self.month > 12:
            raise DateTimeError("month", self.month, "between 1 and 12")
        elif not isinstance(self.day, int):
            raise DateTimeError("day", self.day, "an integer")
        elif self.day < 1 or self.day > 31:
            raise DateTimeError("day", self.day, "between 1 and 31")
        elif self.month == 1 and self.day > 31:
            raise DateTimeError("January", self.day, 'between 1 and 31')
        elif self.month == 2 and self.day > 29:
            raise DateTimeError("Feburary", self.day, "between 1 and 29")
        elif (self.year % 4) != 0 and self.month == 2 and self.day > 28:
            raise DateTimeError("Feburary not in leap year", self.day, "between 1 and 28")
        elif self.month == 3 and self.day > 31:
            raise DateTimeError("March", self.day, 'between 1 and 31')
        elif self.month == 4 and self.day > 30:
            raise DateTimeError("April", self.day, 'between 1 and 30')
        elif self.month == 5 and self.day > 31:
            raise DateTimeError("May", self.day, 'between 1 and 31')
        elif self.month == 6 and self.day > 30:
            raise DateTimeError("June", self.day, 'between 1 and 30')
        elif self.month == 7 and self.day > 31:
            raise DateTimeError("July", self.day, 'between 1 and 31')
        elif self.month == 8 and self.day > 31:
            raise DateTimeError("August", self.day, 'between 1 and 31')
        elif self.month == 9 and self.day > 30:
            raise DateTimeError("September", self.day, 'between 1 and 30')
        elif self.month == 10 and self.day > 31:
            raise DateTimeError("October", self.day, 'between 1 and 31')
        elif self.month == 11 and self.day > 30:
            raise DateTimeError("November", self.day, 'between 1 and 30')
        elif self.month == 12 and self.day > 31:
            raise DateTimeError("December", self.day, 'between 1 and 31')

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"


class DateTime(Date):
    def __init__(self, year, month, day, hour, minutes, seconds):
        super().__init__(year, month, day)
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        if not isinstance(self.hour, int):
            raise DateTimeError("hour", self.hour, "an integer")
        elif self.hour < 0 or self.hour > 23:
            raise DateTimeError("hour", self.hour, "between 0 and 23")
        elif not isinstance(self.minutes, int):
            raise DateTimeError("minutes", self.minutes, "an integer")
        elif self.minutes < 0 or self.minutes > 59:
            raise DateTimeError("minutes", self.minutes, "between 0 and 59")
        elif not isinstance(self.seconds, int):
            raise DateTimeError("seconds", self.seconds, "an integer")
        elif self.seconds < 0 or self.seconds > 59:
            raise DateTimeError("seconds", self.seconds, "between 0 and 59")

    def display(self):
        print(f"{super().__str__()}")
        print(f"{self.hour}:{self.minutes}:{self.seconds}")


class DateTimeError(Exception):
    def __init__(self, value, wrong_value, message):
        self.value = value
        self.wrong_value = wrong_value
        self.message = message

    def __str__(self):
        return f"Invalid value: {self.wrong_value} for {self.value}. It must be {self.message}"


date = DateTime(201, 2, 29, 12, 50, 20)
date.display()
