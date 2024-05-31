# Time-Calculator
The function add_time calculates the new time by adding a specified duration to a given start time, optionally including the day of the week.
It begins by defining a list of days for reference and converting the given day to lowercase for comparison. The start time is split into hours, minutes, and period (AM/PM), and validation checks ensure the input time and duration are within valid ranges. The start time is then converted to a 24-hour format. The duration is split into hours and minutes, and the total time in minutes is calculated by summing the converted start time and the duration. The new time is computed by converting the total minutes back to hours and minutes, and the appropriate period (AM/PM) is determined. The function also handles conversion back to the 12-hour format and ensures minutes are displayed in two-digit format. If the day of the week is provided, it calculates the new day by accounting for the days passed. Finally, the function constructs the new time string, appending the day and the number of days passed if necessary, and returns this string. For example, calling add_time('8:16 PM', '466:02', 'tuesday') would yield the new time including the correct day of the week.
