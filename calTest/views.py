from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def calendar(request, yyyy, mm):
    YEAR = int(yyyy);
    MONTH = int(mm);

    allday = 0;
    yundal = 0;
    maxday = maxDay(YEAR, MONTH);

    allday = (YEAR-1)*365 + (YEAR-1)/4 - (YEAR-1)/100 + (YEAR-1)/400;

    if(MONTH == 1):
        allday = allday;
    else:
        for n in range(1,MONTH):
            allday = allday + maxDay(YEAR, n);

    allday = allday + 1;

    return render_to_response('calendar.html', {'y' : yyyy, 'm' : mm, 'max' : maxday, 'dayInMonth' : calendarOfMonth(mm, allday%7, maxday)})

def maxDay(yyyy, mm):
    YEAR = int(yyyy);
    MONTH = int(mm);

    if((mm == 1) | (mm == 3) | (mm == 5) | (mm == 7) | (mm == 8) | (mm == 10) | (mm == 12)) :
        return 31;
    elif((mm == 4) | (mm == 6) | (mm == 9) | (mm == 11)):
        return 30;
    elif(mm == 2):
        if( ((YEAR%4)==0)&((YEAR%100)!=0)|((YEAR%400)==0) ) :
            yundal=29;
        else :
            yundal=28;
        return yundal;

def calendarOfMonth(mm, start, max):
    month = int(mm);
    dayStart = int(start);
    maxday = int(max);

    monthDay = range(1, maxday+1);
    monthWeek = [];

    for i in range(dayStart):
        monthDay.insert(0, 0);
    #print(monthDay);

    monthWeek.append(monthDay[0:7])
    monthWeek.append(monthDay[7:14])
    monthWeek.append(monthDay[14:21])
    monthWeek.append(monthDay[21:28])
    monthWeek.append(monthDay[28:maxday+2])
    if(len(monthWeek[4]) > 0):
        for i in range(7-len(monthWeek[4])):
            monthWeek[4].append(0);
        #print("YaHo");
    #print(monthWeek);

    return monthWeek;
