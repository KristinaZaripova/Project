from datetime import datetime # мы импортируем встроенную функциональность из стандартной библиотеки

odds = [1, 3, 5,7,9,11,13,15,17,19, 21, 23, 25, 27, 29]

print(4/0)
right_this_minute = datetime.today().minute
print(right_this_minute)
if right_this_minute in odds:
    print("minute is odd")
else:
    print("minute is not odd")


print("hello world")
