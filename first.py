import time
from datetime import datetime # мы импортируем встроенную функциональность из стандартной библиотеки


odds = [1, 3, 5,7,9,11,
        13,15,17,19, 21, 23,
        25, 27, 29] #литеральный список


for num in range(5):
    time.sleep(6)
    right_this_minute = datetime.today().minute #присваиваем результат вызова метода
    print(right_this_minute)
    if right_this_minute in odds:
        print("minute is odd")
    else:
        print("minute is not odd")

from datetime import datetime
odds =[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61]
for num in range(9):
    right_this_minute=datetime.today().minute
    print(right_this_minute)
    if right_this_minute in odds:
        print('minute is odd')
    else:
        print('minute is not odd')



 
