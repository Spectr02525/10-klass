#Это первая программа на Python в репозитории
"""Эта программа поможет вам вычислить квадратный корень из любого числа
Попробуйте ее усовершенствовать, например, добавив обработку исключений
Обратите также внимание на комментарии. Желательно комментировать
все изменения кода, которые Вы вносите.
Задание:
1. Добавьте проверку введенной пользователем переменной на принадлежность
   ко множеству чисел (что данные, которые ввел пользователь не являются
   символами отличными от цифр). Реализовать это можно с помощью проверки
   условия: if ... elif ... else.
3. Добавьте обработку исключений - при возникновении ошибки из-за неправильно
   введеного значения пользователем, программа должна продолжить работу,
   запросив у пользователя еще одно число.
4. Не забывайте добавлять комментарии к вашему коду.
"""



a = int(input("Введите число: "))

b = a ** 0.5


print(b)

