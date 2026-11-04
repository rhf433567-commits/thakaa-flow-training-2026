employee = {
    "name": "Rahaf",
    "city": "Riyadh",
    "age": 24,
    "skills": ["Python", "SQL", "Data Analysis"],
    "courses": {
        "Python": "done",
        "AI": "in progress"
    }
}

# Add a new skill
employee["skills"].append("Cybersecurity")

# Add a new course
employee["courses"]["Cybersecurity"] = "planned"

# Update course status
employee["courses"]["AI"] = "done"

# Delete city
del employee["city"]

# Add GitHub username
employee["github"] = "RHF433567-commits"

# Print dictionary keys
print("Keys:", employee.keys())

# Print number of skills
print("Skills count:", len(employee["skills"]))

# Print courses
print("Courses:", employee["courses"])

# Use get()
print("Python course:", employee.get("courses").get("Python"))
print("Unknown course:", employee.get("courses").get("Java", "Not found"))

# Employee summary
print(
    f"{employee['name']} has {len(employee['skills'])} skills "
    f"and {len(employee['courses'])} courses. "
    f"GitHub: github.com/{employee['github']}"
)  