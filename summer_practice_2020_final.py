from math import *
from time import time
from random import randint
import tracemalloc

"""Задача о назначении минимального количества исполнителей:
Дано n исполнителей и m работ. Для каждой пары (исполнитель, работа) заданы затраты на выполнение работы wij. Имеется общий бюджет w на выполнение 
всех работ. Требуется найти подмножество исполнителей U и распределение этих исполнителей по работам, при котором не будет превышен бюджет. Требуется
минимизировать количество назначенных исполнителей."""

#Функция печати двумерного массива
def printArr(a):
    for i in range(len(a)):
        for j in range(len(a[0])): print(a[i][j], end='\t')
        print()

#Функция заполнения двумерного массива размера lines x rows случайными целыми числами из диапазона [min_num, max_num]
def randomArr(lines, rows, min_num, max_num):
    arr = []
    for i in range(lines):
        row = []
        for j in range(rows):
            row.append(randint(min_num, max_num))
        arr.append(row)
    return arr

#Функция генерирующая все возможные комбинации работников и записывающая их в список combinations
def generate(number_of_works, number_of_workers, current_work_number, current_combination):
    if (current_work_number == number_of_works - 1):
        for i in range(number_of_workers):
            new_combination = current_combination[:]
            new_combination.append(i)
            check_the_record(new_combination)
            combinations.append(new_combination)
    else:
        for i in range(number_of_workers):
            new_combination = current_combination[:]
            new_combination.append(i)    
            generate(number_of_works, number_of_workers, current_work_number + 1, new_combination)

#Функция, проверяющая, станет ли комбинация новым рекордом и записывающая его в record, если да (минимальное количество разных работников, которые смогут уложиться в бюджет)
def check_the_record(combination):
    if total_summ_is_less_or_equal_to_budget(combination):
        global record
        res = number_of_differen_workers_in_combination(combination)
        if  res < record:
            record = res
            
#Функция возвращает количество уникальных работников в комбинации
def number_of_differen_workers_in_combination(combination):
    arr = [0]*number_of_workers
    for i in range(len(combination)):
        arr[combination[i]] += 1
    res = 0
    for i in range(number_of_workers):
        if arr[i]>0:
            res += 1
    return res
  
#Функция возвращающая true, если комбинация рабочих уложится в бюджет
def total_summ_is_less_or_equal_to_budget(combination):
    summ = 0
    for i in range(len(combination)):
        summ += workers[combination[i]][i]
    if summ <= budget:
        return True
    return False
    
#Функция выбирающая подмножество комбинаций, с минимальным количеством работников из множества всех комбинаций
def choose_the_subset(combinations):
    if record != number_of_workers + 1:
        for i in range(len(combinations)):
            if total_summ_is_less_or_equal_to_budget(combinations[i]) and number_of_differen_workers_in_combination(combinations[i]) == record:
                best_combinations.append(combinations[i])

#def test_the_programm():



#Начало программы
print('Запустить тест или программу: ')
print('1 - тест')
print('2 - программу')
important_choice = int(input())

if important_choice == 1: #Тестовые случаи
    #представлены 3 случая, 
    budget = 10
    number_of_works = 3
    number_of_workers = 3
    record = number_of_workers + 1
    workers = [[10,1,10],[1,10,10],[10,10,1]]
    print('Бюджет: ',budget)
    print('Цены: ')
    printArr(workers)
    combinations = []
    best_combinations = []
    tic = time()
    generate(number_of_works,number_of_workers,0,[])
    choose_the_subset(combinations)
    toc = time()
    print('Время выполнения алгоритма: ',toc - tic)
    print('Комбинации с минимальным количеством уникальных рабочих, которые укладываются в бюджет')
    printArr(best_combinations)
    print('------------------------------------------------------------')
    budget = 10
    number_of_works = 3
    number_of_workers = 3
    record = number_of_workers + 1
    workers = [[10,10,10],[10,10,10],[10,10,10]]
    print('Бюджет: ',budget)
    print('Цены: ')
    printArr(workers)
    combinations = []
    best_combinations = []
    tic = time()
    generate(number_of_works,number_of_workers,0,[])
    choose_the_subset(combinations)
    toc = time()
    print('Время выполнения алгоритма: ',toc - tic)
    print('Комбинации с минимальным количеством уникальных рабочих, которые укладываются в бюджет')
    printArr(best_combinations)
    print('------------------------------------------------------------')
    budget = 10
    number_of_works = 3
    number_of_workers = 3
    record = number_of_workers + 1
    workers = [[3,3,3],[3,3,3],[10,10,10]]
    print('Бюджет: ',budget)
    print('Цены: ')
    printArr(workers)
    combinations = []
    best_combinations = []
    tic = time()
    generate(number_of_works,number_of_workers,0,[])
    choose_the_subset(combinations)
    toc = time()
    print('Время выполнения алгоритма: ',toc - tic)
    print('Комбинации с минимальным количеством уникальных рабочих, которые укладываются в бюджет')
    printArr(best_combinations)
else:
    tracemalloc.start()
    print('Введите бюджет на все работы:')
    budget = int(input())

    print('Введите количество работ:')
    number_of_works = int(input())

    print('Введите количество работников:')
    number_of_workers = int(input())

    #Рекорд - текущее минимальное найденное число работников, которые смогут выполнить все работы, не привысив бюджет
    record = number_of_workers + 1
    #Массив в котором будут храниться цены за выполнение каждым работником каждой работы
    workers = []
    #Список, в котором будут храниться все возможные комбинации
    combinations = []
    #Список, в котором хранятся комбинации из минимального числа рабочих, которые укладываются в бюджет
    best_combinations = []

    print('Хотите заполнить массив с ценами за работу вручную, или сгенерировать случайные значения?')
    print('1 - вручную')
    print('2 - случайно')
    #переменная для выбора варианта заполнения массива
    important_choice = int(input()) 

    if important_choice == 1:
        #Заполним массив суммами, которые нужно заплатить каждому работнику за выполнение каждой работы (строка - работник, столбец - работа)
        for i in range(number_of_workers):
            payments_for_this_worker = []
            for j in range(number_of_works):
                print('Введите сумму, которую получит', i,' работник за ', j, ' работу')
                payments_for_this_worker.append(int(input()))
            workers.append(payments_for_this_worker)    
    else:
        print('Введите минимальное число: ')
        min_num = int(input())
        print('Введите максимальное число: ')
        max_num = int(input())
        workers = randomArr(number_of_workers, number_of_works, min_num, max_num)
        printArr(workers)
        
    tic = time()
    snapshot1 = tracemalloc.take_snapshot()
    generate(number_of_works,number_of_workers,0,[])
    choose_the_subset(combinations)
    snapshot2 = tracemalloc.take_snapshot()
    toc = time()
    top_stats = snapshot2.compare_to(snapshot1,'lineno')
    for stat in top_stats[:100]:
        print(stat)

    print('Время выполнения алгоритма: ',toc - tic)
    print('Комбинации с минимальным количеством уникальных рабочих, которые укладываются в бюджет')
    printArr(best_combinations)
