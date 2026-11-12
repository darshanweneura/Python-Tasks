students = {
    "name": "Darshan",
    "age": 21,
    "Marks": 90
}

students["city"] = "Rajkot"
print("After adding city:", students)

print("Name :", students["name"])
print("Reading Name:", students["name"])

students["Marks"] = 99
print("After updating Marks:", students)

del students["age"]
print("After deleting age:", students)

print("Updated dictionary:", students)