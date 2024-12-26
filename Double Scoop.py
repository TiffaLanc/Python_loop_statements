# Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) 
# for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over 
# the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.
# Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"

import random
week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
time_of_day = ['at twilight', 'at midnight' , 'at the witching hour']
mood = ['happy', 'foggy', 'sappy', 'groggy', 'sassy', 'classy' ]

for i in week_day:
    for x in time_of_day:
        print(f"On {i} {x}, you were {random.choice(mood)}.")


    
