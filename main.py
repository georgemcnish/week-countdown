# Lesson Countdown
# Counts down the lessons remaining of the school week
# By George McNish

import calendar, time
from datetime import date, datetime

currentDay = calendar.day_name[date.today().weekday()]
currentTime = datetime.now().time()

currentDay = 'Wednesday'

timings = {'normal': [['08:50','09:50'],['09:53','10:53'],['11:33','12:33'],['13:11','14:11'],['14:14','15:14']],
           'alternative': [['08:50','09:50'],['10:30','11:30'],['12:08','13:08'],['13:11','14:11']]}

days = [['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],[5,5,4,5,5,0,0]]


def countDays(timings, currentDay, currentTime, days):
    lessonCount = 0
    if currentDay != 'Saturday' and currentDay != 'Sunday':
        if currentDay == 'Wednesday':
            currentTiming = timings['alternative']
        else:
            currentTiming = timings['normal']
        for x in range(0, len(currentTiming)):
            end = datetime.strptime(currentTiming[x][1], '%H:%M').time()
            if currentTime >= end:
                lessonCount = lessonCount + 1
        print(lessonCount)
    for x in range(0, len(days[0])):
        if days[0][x] == currentDay:
            dayIndex = x
    for x in range(0, dayIndex):
        lessonCount = lessonCount + days[1][x]
    return lessonCount

count = countDays(timings, currentDay, currentTime, days)

percentage = int((count / 24) * 100)

percentage = str(percentage) + '%'
outputText = '{} out of 24 lessons complete'.format(str(count))
alternativeOutputText = '{} lessons completed today'.format(str(count))
