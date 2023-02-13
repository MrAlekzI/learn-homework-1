"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def str_check(string_1, string_2):
      if isinstance(string_1, str) and isinstance(string_2, str): 
        if string_1 == string_2:
          return 1
        elif string_1 != string_2 and len(string_1) > len(string_2):
          return 2
        elif string_1 != string_2 and string_2 == 'learn':
          return 3
      else:
        return 0

    
    print(str_check('abcd', 'abcd'))
    print(str_check('abcd', 'abc'))
    print(str_check('abcd', 'learn'))
    print(str_check('abcd', True))
    
if __name__ == "__main__":
    main()
