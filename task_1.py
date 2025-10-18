# Софія дала вам свій розклад і дві дати і сказала, що їй потрібно розпланувати свої вихідні. Вона просить вас порахувати, 
# скільки вихідних (субота і неділя) буде починаючи з першої дати і закінчуючи другою. Якщо граничні дати випадають на вихідний, 
# то враховуйте їх теж.
# Дати задані, як тип даних datetime.date (Детальніше можете прочитати тут). Результат повинен бути цілим числом.
# Вхідні дані: Початкова й кінцева дата, як datetime.date.
# Вихідні дані: Кількість вихідних днів між цими датами, як ціле число (int).
# Приклади:
# 1
# checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2
# 2
# checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8
# 3
# checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2Як це використовується: Гарна можливість навчитися працювати з датами. 
# Ці методи часто використовуються календарних додатках, в автоматичних системах сповіщень та інших подібних областях.
# Передумова: start_date < end_date.

from datetime import date, timedelta

def checkio(start_date, end_date):
    weekends = 0
    current_date = start_date
    while current_date <= end_date:
        day = current_date.weekday()
        if day == 5 or day == 6: 
            weekends += 1
        current_date += timedelta(days=1)
    return weekends 


if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
    
    
print(checkio(date(2013, 9, 18), date(2013, 9, 23)) )
print(checkio(date(2013, 1, 1), date(2013, 2, 1))) 
print(checkio(date(2013, 2, 2), date(2013, 2, 3)))