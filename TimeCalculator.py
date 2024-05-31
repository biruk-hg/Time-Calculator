def add_time(start, duration, day=""):

    #To find the correct day for the new time
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = day.lower()
    index = next((i for i, d in enumerate(days) if d.lower() == day), -1)

    #Splits start input into the time and period
    time_start = start.split()
    clock = time_start[0]
    period_of_day = time_start[1]

    #Split start into hours and minutes
    start_hour_minute = time_start[0].split(':')
    start_hour = int(start_hour_minute[0])
    start_minutes = int(start_hour_minute[1])

    #Checking for valid start input
    if(start_hour > 12 or start_minutes >= 60):
        return f'Start time {start} is invalid!'

    #Converts it to 24-hour clock system
    if period_of_day == 'PM' and start_hour != 12:
        start_hour += 12
    elif period_of_day == 'AM' and start_hour == 12:
        start_hour = 0
    
    #Splits duration into hours and minutes
    time_duration = duration.split(':')
    duration_hour = int(time_duration[0])
    duration_minutes = int(time_duration[1])

    #Checking for a valid duration input
    if(duration_minutes >= 60):
        return f'Duration minute {duration} is invalid!'

    #Calculate the total minutes
    total_mins = (start_hour*60) + start_minutes + (duration_hour*60) + duration_minutes

    #Calculate the new hour and minutes
    new_hour = (total_mins // 60) % 24
    new_mins = total_mins % 60

    #Setting period
    new_period = 'AM'
    if new_hour >= 12:
        new_period = 'PM'

    #Changing back to 12-hour system
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    #Changing mins from single-digit to two-digits
    if new_mins <= 9:
        new_mins = str(0) + str(new_mins)
    
    #Calculate number of days that passed
    days_passed = (total_mins) // (24 * 60)
    new_day_index = (index + days_passed) % 7 

    new_time = f"{new_hour}:{new_mins} {new_period}"

    day_message = ''
    if days_passed == 1:
        day_message = ' (next day)'
    elif days_passed > 1:
        day_message = f' ({days_passed} days later)'
    else:
        day_message = ''

    #Adding the day of the week if provided
    if day:
        new_day = days[new_day_index]
        new_time += f', {new_day}{day_message}'
    else:
        new_time += day_message
    
    # new_time = f"{new_hour}:{new_mins} {new_period} {new_day} {day_message}"

    return new_time
