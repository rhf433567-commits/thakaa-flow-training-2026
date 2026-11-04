registered = [
    "sara@mail.com",
    "omar@mail.com",
    "lina@mail.com",
    "sara@mail.com",
    "yousef@mail.com",
    "nora@mail.com"
]

attended = [
    "omar@mail.com",
    "lina@mail.com",
    "khaled@mail.com",
    "nora@mail.com"
]

tickets = ["VIP", "Regular", "Regular", "Student", "VIP", "Regular"]

prices = {
    "VIP": 450,
    "Regular": 200,
    "Student": 100
}

registered_set = set(registered)
attended_set = set(attended)

print("Registered:", sorted(registered_set))
print("Attended:", sorted(attended_set))

print("Duplicates:", len(registered) - len(registered_set))

print("Attended and registered:", sorted(registered_set & attended_set))
print("Registered but not attended:", sorted(registered_set - attended_set))
print("Attended but not registered:", sorted(attended_set - registered_set))

attendance_rate = len(registered_set & attended_set) / len(registered_set) * 100

print("Attendance rate:", attendance_rate, "%")

vip_count = tickets.count("VIP")
regular_count = tickets.count("Regular")
student_count = tickets.count("Student")

revenue = (
    vip_count * prices["VIP"]
    + regular_count * prices["Regular"]
    + student_count * prices["Student"]
)

print("VIP tickets:", vip_count)
print("Regular tickets:", regular_count)
print("Student tickets:", student_count)
print("Total revenue:", revenue)

print("Sorted report:", sorted(registered_set))