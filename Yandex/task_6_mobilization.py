"""В Яндексе снова стартует проект «Мобилизация»! Компания набирает на трёхмесячную подготовку n молодых людей,
увлечённых мобильной разработкой. В начале проекта был проведён тест, где скилл участника i в разработке был оценен
как ai, а скилл в управлении как bi.

На время проекта участников необходимо разделить на две равные по количеству участников команды — разработчиков и
менеджеров. Планируется сделать это таким образом, чтобы максимизировать суммарную пользу, приносимую всеми
участниками. Если участнику достанется роль разработчика, его польза будет равняться ai, в противном случае — bi.

Но даже занятые проектом, участники находят время для получения новых знаний! Иногда участники приносят сертификаты о
прохождении курсов, где сказано, что скилл участника i в разработке или же в управлении увеличился на di. В таком
случае может быть выгодно переформировать команды для максимизации суммарной пользы (равные размеры команд необходимо
сохранить).

Ваша задача помочь Яндексу и после рассмотрения каждого нового принесённого участником сертификата посчитать текущую
суммарную пользу команд.

Формат ввода В первой строке входного файла дано число n (2 ≤ n ≤ 2 ⋅ 105, n — чётное) — количество участников
проекта. Вторая строка задаёт n целых чисел ai (0 ≤ ai ≤ 109) — скилл каждого из участников в разработке. Следующая
строка в том же формате задаёт скилл участников в управлении bi (0 ≤ bi ≤ 109).

Следующая строка содержит целое число m (1 ≤ m ≤ 105) — количество принесённых участниками сертификатов. Каждая из
следующих m строк содержит три целых числа numi, typei, di (1 ≤ numi ≤ n, 1 ≤ typei ≤ 2, 1 ≤ di ≤ 104) — номер
участника, тип увеличиваемого скилла (1 — разработка, 2 — управление) и значение увеличения соответствующего навыка.

Формат вывода
После обработки каждого запроса на поступление нового сертификата выведите текущую суммарную пользу всех участников.
Пример 1.
Ввод
4
7 15 3 4
10 10 0 6
3
1 1 4
4 1 6
2 2 10
Вывод
34
35
43"""

"""
try:
    number_people = int(input())
    if 2 <= number_people <= 210 and number_people % 2 == 0:
        pass
    else:
        raise ValueError()

    list_develop = [int(item) for item in input().split()]
    if len(list_develop) != number_people:
        raise ValueError()
    for item in list_develop:
        if 0 <= item <= 109:
            pass
        else:
            raise ValueError()

    list_manager = [int(item) for item in input().split()]
    if len(list_manager) != number_people:
        raise ValueError()
    for item in list_manager:
        if 0 <= item <= 109:
            pass
        else:
            raise ValueError()

    number_certificate = int(input())
    if 1 <= number_certificate <= 105:
        pass
    else:
        raise ValueError()

    list_certificate = []
    for item in range(number_certificate):
        list_certificate.append([int(item) for item in input().split()])

    for item, result in enumerate(list_certificate):
        if 1 <= list_certificate[item][0] <= number_people \
                and 1 <= list_certificate[item][1] <= 2 \
                and 1 <= list_certificate[item][2] <= 104:
            pass
        else:
            raise ValueError()


except ValueError:
    print("Oops!  That was no valid number.  Try again...")
    exit()
"""
number_people = 4
list_develop = [7, 15, 3, 4]
list_manager = [10, 10, 0, 6]
number_cert = 2
list_cert = [[1, 1, 4], [4, 1, 6], [2, 2, 10]]




def sort_people():
    top_develop = []
    top_manager = []

    for (dev, man) in zip(list_develop, list_manager):
        if dev > man:
            top_develop.append(dev)
        else:
            top_manager.append(man)

    max_number_dev = sum(top_develop)
    max_number_man = sum(top_manager)
    print(max_number_man + max_number_dev)

def sort_certificate():
    # checking for duplicates in the sheets
    kopy_develop = []
    kopy_manager = []
    count = 0
    if len(set(list_manager)) != len(list_manager):
        for i in range(len(list_manager)):
            count += 1
            kopy_manager.append(count)
    else:
        kopy_manager = list_manager
    if len(set(list_develop)) != len(list_develop):
        for i in range(len(list_manager)):
            count += 1
            kopy_develop.append(count)
    else:
        kopy_develop = list_develop

    for (dev, man, cert) in zip(list_develop, list_manager, list_cert):
        for i in range(number_people):
            if kopy_develop.index(kopy_develop[i]) + 1 == cert[0] and cert[1] == 1:
                list_develop[i] += cert[2]

    for (dev, man, cert) in zip(list_develop, list_manager, list_cert):
        for i in range(number_people):
            if kopy_manager.index(kopy_manager[i]) + 1 == cert[0] and cert[1] == 2:
                list_manager[i] += cert[2]




"""num = list_certificate[0]
type = list_certificate[1]
d = list_certificate[2]

print(num, type, d)"""




