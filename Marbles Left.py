def week (month, day, year):
    '''(int, int, int) -> int

    Takes the date and returns the week of the year

    >>>week(6, 16, 2013)
    24
    >>>week(3,14,2007)
    11
'''

    import datetime
    
    return datetime.date(year, month, day).isocalendar()[1]

def weeks_left (month, day, year):
    '''(int,int,int) -> int

    Takes the years left until 18 and converts to weeks

    >>> weeks_left(6, 16, 2013)
    912
    >>> weeks_left(3,14,2007)
    665
'''

    import datetime

    import time
    ## yyyy format
    current_date = (time.strftime("%d,%m,%Y"))
    current_year = (time.strftime("%Y"))
    ##int(current_year)
    birth_week = week(current_date)
    years_old = current_year - year

    return birth_week
    

    '''
    years_old = current_year - year
    years_left = 18 - years_old
            
    weeks_remaining = years_left * 52
            
    add_weeks = week(month, day, year) + weeks_remaining
    
    return add_weeks'''

    
