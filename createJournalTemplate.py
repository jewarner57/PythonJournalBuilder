import datetime
from pathlib import Path
import calendar

def getClosestMonday(startDate):

    print("Starting...")
    weekday = startDate.weekday();
    day = startDate.day
    month = startDate.month
    year = startDate.year

    #get the date of the closest Monday
    closestMonday = day
    if weekday > 3:
        daysBeforeMonday = 7-weekday
        closestMonday = day + daysBeforeMonday
    elif weekday <= 3:
        daysBeforeMonday = -1*(weekday)
        closestMonday = day + daysBeforeMonday

    print("Closest Monday is " + str(month) + "/" + str(closestMonday))
    return (year, month, closestMonday)

def correctInvalidDates(date):

    #test for invalid dates
    year = date[0]
    month = date[1]
    day = date[2]

    maxDays = calendar.monthrange(year, month)
    if day < 1:
        if month != 1:
            prevMonthMaxDays = calendar.monthrange(year, month-1)
            day = prevMonthMaxDays[1]-day
            month-=1
        elif month == 1:
            year -= 1
            month = 12
            prevMonthMaxDays = calendar.monthrange(year, month)
            day = prevMonthMaxDays[1]-(day*-1)

    if day > maxDays[1]:
        day -= maxDays[1]

        if month != 12:
            month += 1
        elif month == 12:
            month = 1
            year += 1

    return(datetime.datetime(year, month, day))


def getWeekdays(startDate):
    weekdays = [startDate]
    counter = 1

    while len(weekdays) < 5:
        weekdays.append(correctInvalidDates((weekdays[counter-1].year, weekdays[counter-1].month, weekdays[counter-1].day+1)))
        counter+=1
    return weekdays

def writeFile(journalDays):
    startDay = journalDays[0]
    endDay = journalDays[len(journalDays)-1]

    print("Writing dates: " + str(startDay.month)+"/"+str(startDay.day)+"-"+str(endDay.month)+"/"+str(endDay.day))

    newFile  = open(str(startDay.month)+":"+str(startDay.day)+"-"+str(endDay.month)+":"+str(endDay.day) + " Journal.md", "w")

    newFile.write("## "+ str(startDay.year) +" Daily Learning Journal : " + str(startDay.month)+"/"+str(startDay.day)+"-"+str(endDay.month)+"/"+str(endDay.day))

    counter = 0
    while counter < 5:
        newFile.write("\n* * *")
        newFile.write("\n### " + str(calendar.day_name[journalDays[counter].weekday()]) + " " + str(journalDays[counter].month)+"/"+str(journalDays[counter].day))
        newFile.write("\n* * *")
        newFile.write("\n#### What did you do today?")
        newFile.write("\n* _")
        newFile.write("\n#### What did learn today?")
        newFile.write("\n* _")
        newFile.write("\n#### 2-3 Questions you still have")
        newFile.write("\n* _")
        counter+=1

    newFile.close()
    print("...Done")

#get the first day of the journal
startDay = correctInvalidDates(getClosestMonday(datetime.datetime.now()))
#get the rest of the weekdays
weekdays = getWeekdays(startDay)
#write the new journal
writeFile(weekdays)