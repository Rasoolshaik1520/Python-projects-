# #the program to display the current time with the greeting!!
# #import the time module
# import time
# #to get the current time
# hour = time.strftime('%H')
# minute = time.strftime('%M')
# second = time.strftime('%S')

# #to print the greeting with current time
# if 5 <= hour < 12:
#     greeting = "good morning"
# elif 12 <= hour < 17:
#     greeting = "good afternoon"
# elif 16 <= hour < 18:
#     greeting = "good evening"
# else:
#     greeting = "good night"

# print(f"{greeting}! the current time is{hour}:{minute}:{second}")



import time  # This lets us use time-related functions

# Get the current hour, minute, and second from the system clock
hour = int(time.strftime('%H'))     # Hour in 24-hour format (00 to 23)
minute = time.strftime('%M')        # Minute (00 to 59)
second = time.strftime('%S')        # Second (00 to 59)

# Decide what greeting to show based on the hour
if 5 <= hour < 12:
    greeting = "Good Morning"
elif 12 <= hour < 17:
    greeting = "Good Afternoon"
elif 17 <= hour < 21:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

# Print the greeting and the current time in HH:MM:SS format
print(f"{greeting}! The current time is {hour}:{minute}:{second}")
