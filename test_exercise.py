import string
import math

"""This method prepares input data for further conversion
Данный метод подготавливает входные данные для последующей конвертации"""


def data_preparation():
    data_in = input("Введите текст: ")#
    while data_in.isspace() or data_in == '' or str.isdigit(data_in):
        print ("Строка должна содержать хотя бы одну букву")
        data_in = input("Введите хотя бы один символ: ")

    lower_case = list(data_in.lower())  # Converting to capital letters / Делаем входные данные прописными
    # буквами
    filter_letters = list(filter(lambda letter: (letter >= 'a') & (letter <= 'z'), lower_case))

    # Производим фильтрацию элементов списка. Здесь изначально хотелось осуществить логику с помощью регулярных выражений,
    # но они менее удобочитаемы

    def convert_letters():
        for i in filter_letters:
            answer = string.ascii_lowercase.index(i) + 1  # В данном случае использовался импорт модуля string и задача
        # осуществлялась с помощью методов модуля. !!!НО!!! также данную задачу можно решить и без модуля, например:
        # print(ord('a') - 96)
            print(answer)
        return answer


    convert_letters()


data_preparation()
