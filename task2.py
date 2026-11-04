tasks = ["Update website", "Client meeting", "Code review"]

tasks.append("Write report")
tasks.insert(0, "Fix urgent bug")

removed = tasks.pop()
print("Removed:", removed)

tasks.remove("Client meeting")
tasks.insert(1, "Review Rahaf's code")

print("Number of tasks:", len(tasks))
print("First task:", tasks[0])
print("Last task:", tasks[-1])

print("Sorted copy:", sorted(tasks))
print("Original list:", tasks)

tasks.sort()
print("After sort:", tasks)