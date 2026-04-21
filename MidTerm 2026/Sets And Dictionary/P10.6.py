# Program to delete elements from a dictionary

student = {
    "name": "Prachi Sharma",
    "age": 19,
    "course": "B.Sc Nursing"
}
student.pop("age")
del student["course"]
# student.clear() // Remove All Values And Keys
print(student)