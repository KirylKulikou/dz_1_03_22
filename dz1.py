duration = int(input('введите кол-во секунд :'))
second = duration
print('duration =',duration)
print(second, 'сек')
duration = int(input('введите кол-во секунд :'))
sec = duration % 60
min = duration // 60
print('duration =',duration)
print(min, "мин", sec, "сек")
duration = int(input('введите кол-во секунд :'))
sec = duration % 60
min = duration // 60 % 60
hour = duration // 3600
print('duration =',duration)
print(hour, "час", min, "мин", sec, "сек")
duration = int(input('введите кол-во секунд :'))
sec = duration % 60
min = duration // 60 % 60
hour = duration // 3600 % 24
day = duration // (24 * 3600)
print('duration =',duration)
print(day, "дн", hour, "час", min, "мин", sec, "сек")