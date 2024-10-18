# Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) 
# for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over 
# the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.
# Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"

import random
week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
time_of_day = ['morning', 'afternoon', 'evening']
mood = ['happy', 'foggy', 'sappy', 'groggy', 'sassy', 'classy' ]

daily_mood = random.choice(mood)
what_time = random.choice(time_of_day)
wk_day = random.choice(week_day)


for i in range(5):week_day
for i in range(3): time_of_day
print("On " +wk_day , what_time + " I felt " + daily_mood ) 

#I haven't quite figured out the nested loop


    
