def add_time(start, duration, day=None):
    days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    split = start.split()
    split2 = split[0].split(':')
    hour = int(split2[0])
    minute = int(split2[1])
    time = split[1]

    duration = duration.split(':')
    hour2 = int(duration[0])
    minute2 = int(duration[1])

    minuteFinal = minute + minute2
    hourFinal = 0
    if minuteFinal > 59:
        minuteFinal -= 60
        hourFinal += 1

    hourFinal += hour
    hourFinal += hour2

    daysLater = 0

    if hourFinal > 24:
        daysLater = round(hourFinal / 24)
        hourFinal = int(hourFinal % 24)

    if hourFinal > 12:
        hourFinal -= 12
        if time == 'PM':
            time = 'AM'
            if daysLater == 0:
                daysLater += 1
        else:
            time = 'PM'
    elif hourFinal == 12:
        if time == 'PM':
            time = 'AM'
        else:
            time = 'PM'

    if day is not None:
        day = day.lower()
        index = days_of_the_week.index(day)
        next_day = index + daysLater
        if next_day > 6:
            next_day = next_day % 7

    FinalString = ""
    FinalString += str(hourFinal)
    FinalString += ':'
    if minuteFinal < 10:
        FinalString += '0'
    FinalString += str(minuteFinal)
    FinalString += ' '
    FinalString += time

    if day is not None:
        FinalString += ', '
        FinalString += days_of_the_week[next_day].capitalize()

    if daysLater == 1:
        FinalString += ' (next day)'
    elif daysLater > 1:
        FinalString += ' ('
        FinalString += str(daysLater)
        FinalString += ' days later)'

    return FinalString



print(add_time("11:43 PM", "24:20", "tueSday"))
