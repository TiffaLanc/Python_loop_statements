# Task 1: Your Mood Today Write a program that prints off different moods for each day of the week. Create a list of moods such as 
# "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it. 
# Ensure that your program includes the use of the random module to select the mood. Example Outcome: An example output could be "On Wednesday, you were feeling happy." 
# "On Thursday you were feeling sad."

import random

day_of_the_week = ['Monday', 'Tuseday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mood = ['happy', 'sad', 'hopeful', 'excited', 'alert', 'enthusiastic', 'concerned']
daily_mood = random.choice(mood)
what_day = random.choice(day_of_the_week)

for day_of_the_week in day_of_the_week : range(8)
for mood in mood : range(8)
print('On ' +what_day,' I felt ' + str(daily_mood))