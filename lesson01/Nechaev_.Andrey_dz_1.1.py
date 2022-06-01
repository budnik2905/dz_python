duration = int(input('Введите время в секундах: '))
hours = duration // 3600
minutes = (duration // 60) % 60
seconds = duration % 60
if duration >= 3600:
    print(hours, ' час', minutes, ' мин',seconds, 'сек')
if duration < 3600 and duration >= 60:
    print(minutes, ' мин',seconds, 'сек')
if duration < 60 :
    print(seconds,' сек')

