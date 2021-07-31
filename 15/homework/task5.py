from datetime import datetime

birth_date = input("Введите ваш день рождения в формате день/месяц/год\n")

date = datetime.strptime(birth_date, "%d/%m/%Y")


def name_month(month):
    if month == 1:
        return "января"
    elif month == 2:
        return "февраля"
    elif month == 3:
        return "марта"
    elif month == 4:
        return "апреля"
    elif month == 5:
        return "мая"
    elif month == 6:
        return "июня"
    elif month == 7:
        return "июля"
    elif month == 8:
        return "августа"
    elif month == 9:
        return "сентября"
    elif month == 10:
        return "октября"
    elif month == 11:
        return "ноября"
    elif month == 12:
        return "декабря"


print(f"Вы родились в {date.year}, {date.day} {name_month(date.month)}")
