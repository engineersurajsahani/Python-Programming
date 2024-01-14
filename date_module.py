# Date Module

from datetime import datetime, date, time, timedelta

# Example 1: Getting the current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# Example 2: Creating a specific date
specific_date = date(2022, 7, 15)
print("Specific Date:", specific_date)

# Example 3: Creating a specific time
specific_time = time(14, 30)
print("Specific Time:", specific_time)

# Example 4: Formatting dates
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# Example 5: Parsing a string to a datetime object
date_string = "2022-07-15 14:30:00"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Datetime:", parsed_datetime)

# Example 6: Performing operations with timedelta
future_date = current_datetime + timedelta(days=7)
print("Future Date:", future_date)
