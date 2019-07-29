"""
Input the date in dd/mm/yyyy format (dateStr)
Split dateStr into day, month and year strings
Convert the month string into a month number
Use month number to look up the month name
Create a new date string in form Day Month, Year
Output new date string
"""

    monthList = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "October",
        "November",
        "December"
    ]
    dateList = dateStr.split("/")
    monthNum = int(dateList[1])
    dayNum = int(dateList[0])

    stndrdth = ""
    if(dayNum % 10 == 1 and dayNum != 11):
        stndrdth = "th"
    elif(dayNum % 10 == 2 and dayNum != 12):
        stndrdth = "nd"
    elif(dayNum % 10 == 3 and dayNum != 13):
        stndrdth = "rd"
    else:
        stndrdth = "th"

    return "%d%s of %s, %s" % (dayNum, stndrdth, monthList[monthNum - 1], dateList[2])


print(dateConvert(input("Enter your date in dd/mm/yyyy format: ")))
