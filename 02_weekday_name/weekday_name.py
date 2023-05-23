def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if day_of_week > len(days) or day_of_week < 0:
        return None
    week_days = [1, 2, 3, 4, 5, 6, 7]
    for day in week_days:
        if day_of_week == day:
            return days[day-1]
        
print('day of the week: Saturday', weekday_name(7))
print('day of the week: None', weekday_name(0))
print('day of the week: None', weekday_name(8))
print('day of the week: Sunday', weekday_name(1))