MISSION_DAYS = 70

crew = ("Nora", "Omar", "Lina", "Yousef")

supplies = {
    "oxygen_kg": 840,
    "water_l": 1260,
    "food_kg": 336
}

per_person_daily = {
    "oxygen_kg": 0.84,
    "water_l": 3.5,
    "food_kg": 1.2
}

days_left = {
    "oxygen_kg": supplies["oxygen_kg"] / (per_person_daily["oxygen_kg"] * len(crew)),
    "water_l": supplies["water_l"] / (per_person_daily["water_l"] * len(crew)),
    "food_kg": supplies["food_kg"] / (per_person_daily["food_kg"] * len(crew))
}

print("Days left:", days_left)

weakest_resource = min(days_left, key=days_left.get)

print("Weakest resource:", weakest_resource)
print("Days available:", days_left[weakest_resource])

if days_left[weakest_resource] >= MISSION_DAYS:
    print("Mission is possible")
else:
    print("Mission is not possible")
    print("Shortage days:", MISSION_DAYS - days_left[weakest_resource])

telescope_a = {"Kepler-22b", "Proxima b", "TRAPPIST-1e", "Gliese 667Cc"}
telescope_b = {"Proxima b", "TRAPPIST-1e", "HD 40307g"}

print("Common planets:", telescope_a & telescope_b)
print("A only:", telescope_a - telescope_b)
print("All planets:", telescope_a | telescope_b)

mission_log = [
    "Mission started",
    "Crew checked resources",
    "Telescopes scanned planets"
]

print("Last event:", mission_log[-1])
print("Total events:", len(mission_log)) 
