# Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

from random import choice

list1 = ["курс", "гикбрейнс", "куратор", "учитель", "студент"]
list2 = ["вчера", "сегодня", "завтра", "позавчера", "послезавтра"]
list3 = ["смешной", "яркий", "вдохновляющий", "заманчивый", "интересный"]
list_1 = []


def get_jokes(n, flag=False):
    for i in range(n):
        random_index = choice(list1)
        random_index_1 = choice(list2)
        random_index_2 = choice(list3)
        joke = f'{random_index} {random_index_1} {random_index_2}'
        list_2 = []
        print(joke)
        if flag == True:
            list_2 = joke.split()
            for noun in list1:
                for fun in list_2:
                    if noun == fun:
                        list1.remove(noun)

            for adverb in list2:
                for fun in list_2:
                    if adverb == fun:
                        list2.remove(adverb)


            for adjective in list3:
                for fun in list_2:
                    if adjective == fun:
                        list3.remove(adjective)

n = int(input('Укажите количество шуток: '))
get_jokes(n, flag=True)


























