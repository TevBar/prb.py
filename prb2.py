import random 

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
moods = ['happy', 'sad', 'energetic', 'calm']
time_of_day = ['morning', 'afternoon', 'evening', 'night']

for day in days_of_week:
    for i in range(1):
        mood = random.choice(moods)
        time = random.choice(time_of_day)
        print(f"on {day} i feel {mood} in the {time}.")
