
import re

reg = input("Register Number: ")
email = input("Institutional Email: ")
course = input("Course Code: ")
semester = input("Semester: ")
mobile = input("Mobile Number: ")

checks = {
    "Register Number": bool(
        re.fullmatch(r"\d{12}", reg)
    ),
    "Institutional Email": bool(
        re.fullmatch(
            r"[A-Za-z0-9._%+-]+@simats\.edu\.in", email
        )
    ),
    "Course Code": bool(
        re.fullmatch(r"[A-Z]{2,4}\d{2,3}", course)
    ),
    "Semester": bool(
        re.fullmatch(r"[1-8]", semester)
    ),
    "Mobile Number": bool(
        re.fullmatch(r"[6-9]\d{9}", mobile)
    )
}

print("\nREGISTRATION REPORT")

for field, valid in checks.items():
    print(field + ":", "Valid" if valid else "Invalid")

if all(checks.values()):
    print("Registration Status: Successful")
else:
    print("Registration Status: Failed")
