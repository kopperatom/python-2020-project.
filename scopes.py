import datetime

def get_day_of_the_week(target):
    try:
        thisDate =datetime.datetime.strptime(target,"%Y-%m-%d")
        dayofweek = thisDate.strftime("%A")
        return dayofweek
    except:
        return "invalid YYYY-MM-DD date"

print(get_day_of_the_week("2002-12-26"))    
