"""
Чтобы не мешать коллегам на рабочем месте громкими обсуждениями, ребята назначают встречи на определенное время
и бронируют переговорки. При бронировании нужно указать дату и время встречи, её длительность и список участников.
Если у кого-то из участников получается две встречи в один и тот же момент времени, то в бронировании будет отказано
с указанием списка людей, у которых время встречи пересекается с другими встречами. Вам необходимо реализовать
прототип такой системы.

Формат ввода
В первой строке входного файла содержится одно число n (1 ≤ n ≤ 1000) — число запросов.

В следующих n строках содержатся запросы по одному в строке. Запросы бывают двух типов:

APPOINT day time duration k names1 names2… namesk
PRINT day name
day — номер дня в 2018 году (1 ≤ day ≤ 365)

time — время встречи, строка в формате HH:MM (08 ≤ HH ≤ 21, 00 ≤ MM ≤ 59)

duration — длительность встречи в минутах (15 ≤ duration ≤ 120)

k — число участников встречи (1 ≤ k ≤ 10)

namesi, name — имена участников, строки, состоящие из маленьких латинских букв (1 ≤ |name| ≤ 20).
У всех коллег уникальные имена. Кроме того гарантируется, что среди участников одной встречи ни одно
имя не встречается дважды.

Формат вывода
Если удалось назначить встречу (первый тип запросов), выведите OK.

Иначе выведите в первой строке FAIL, а в следующей строке через пробел список имен участников, для которых время встречи
пересекается с другими встречами, в том порядке, в котором имена были даны в запросе.

Для второго типа запросов выведите для данного дня и участника список всех событий на данный момент в этот день в
хронологическом порядке, по одному в строке, в формате

HH:MM duration names1 names2 … namesk

где имена участников следуют в том же порядке, что и в исходном описании встречи. Если событий в данный день для этого
человека нет, то ничего выводить не нужно.
Пример 1.
Ввод
7
APPOINT 1 12:30 30 2 andrey alex
APPOINT 1 12:00 30 2 alex sergey
APPOINT 1 12:59 60 2 alex andrey
PRINT 1 alex
PRINT 1 andrey
PRINT 1 sergey
PRINT 2 alex
Вывод
OK
OK
FAIL
alex andrey
12:00 30 alex sergey
12:30 30 andrey alex
12:30 30 andrey alex
12:00 30 alex sergey
"""

try:
    requests = int(input())
    if 1 <= requests <= 1000:
        pass
    else:
        raise ValueError

    list_requests = []

    for item in range(requests):
        list_requests.append([item for item in input().split()])

    list_days = []

    for item, result in enumerate(list_requests):
        list_days.append(list_requests[item][2].split(':'))

    for item, result in enumerate(list_days):
        hours = int(result[0])
        minute = int(result[1])
        if 8 <= hours <= 21 \
                and 0 <= minute <= 59:
            pass
        else:
            raise ValueError

    for item, result in enumerate(list_requests):
        if list_requests[item][0] == 'APPOINT' or 'PRINT' \
                and 1 <= list_requests[item][1] <= 365 \
                and 15 <= list_requests[item][3] <= 120 \
                and 1 <= list_requests[item][4] <= 10 \
                and 1 <= len(list_requests[item]) - 5 <= 20:
            pass

        else:
            raise ValueError


except ValueError:
    print("Oops!  That was no valid number.  Try again...")
    exit()
print(list_requests)
"""type_requests = list_requests[item][0]
day = list_requests[item][1]
time = list_requests[item][2]
duration = list_requests[item][3]
number_people = list_requests[item][4]
list_names = list_requests[item][5]"""


