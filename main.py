from datetime import date

WEEKDAYS = [
        "Понедельник", "Вторник", "Среда", "Четверг",
        "Пятница", "Суббота", "Воскресенье"
    ]
NUMBERS = {
    '0': [
        "*****",
        "*   *",
        "*   *",
        "*   *",
        "*****"
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        " *** "
    ],
    '2': [
        "*****",
        "    *",
        "*****",
        "*    ",
        "*****"
    ],
    '3': [
        "*****",
        "    *",
        "*****",
        "    *",
        "*****"
    ],
    '4': [
        "*   *",
        "*   *",
        "*****",
        "    *",
        "    *"
    ],
    '5': [
        "*****",
        "*    ",
        "*****",
        "    *",
        "*****"
    ],
    '6': [
        "*****",
        "*    ",
        "*****",
        "*   *",
        "*****"
    ],
    '7': [
        " ****",
        "    *",
        "    *",
        "    *",
        "    *"
    ],
    '8': [
        "*****",
        "*   *",
        "*****",
        "*   *",
        "*****"
    ],
    '9': [
        "*****",
        "*   *",
        "*****",
        "    *",
        "*****"
    ]
}
# Функция определяющая, является ли введенный год високосным:
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Функция определяющая день недели для введенной даты:
def get_day_of_week(day, month, year):
    birthday = date(year, month, day)
    return WEEKDAYS[birthday.weekday()]
    

# Функция вычисляющая возраст в данный момент:
def calculate_age(day, month, year):
    today = date.today()
    birthday = date(year, month, day)
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    return age

# Функция вывода даты рождения в стиле электронного табло:
def print_birthday_date(day, month, year):
    date_str = f"{day:02d}{month:02d}{year:04d}"
    patterns = []
    for num in date_str:
        patterns.append(NUMBERS[num])
    for i in range(5):
        for el in range(len(patterns)):
            if el == 2 or el == 4: print(end="   ")
            print(patterns[el][i], end=' ')
        print("")

try:
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))

    date(year, month, day)  
 
    print(f"\nДата рождения: {day:02d}.{month:02d}.{year}")
    print(f"День недели: {get_day_of_week(day, month, year)}")
    print(f"Високосный год: {'Да' if is_leap_year(year) else 'Нет'}")
    print(f"Возраст: {calculate_age(day, month, year)} лет")
    print("\nДата в стиле электронного табло:")
    print_birthday_date(day, month, year)


except ValueError:
    print("Ошибка: введены некорректные данные.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
