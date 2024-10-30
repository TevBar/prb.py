import random

days_of_week = ["monday", "tuesday","wednesday", "thursday", "friday", "saturday", "sunday"]

moods = ["happy","sad", "energetic", "calm"]

for i in range(7):
    mood = random.choice(moods)
    print(f"on {days_of_week[i]} I am {mood}.")

