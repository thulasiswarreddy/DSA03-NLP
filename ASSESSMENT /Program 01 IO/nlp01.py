
import re

resume = """
Name: S THULASISWAR REDDY
Email: eswarsiddi917@gmail.com
Mobile: 7416805738
Skills: Python, Java, SQL, Machine Learning, NLP
Experience: 3 years
"""

name = re.search(r"Name:\s*(.+)", resume)
email = re.findall(r"[\w.-]+@[\w.-]+\.\w+", resume)
mobile = re.findall(r"\b[6-9]\d{9}\b", resume)

skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found = [
    s for s in skills
    if re.search(r"\b" + re.escape(s) + r"\b", resume, re.I)
]

exp = re.search(r"Experience:\s*(\d+)", resume)
years = int(exp.group(1)) if exp else 0

print("RESUME SUMMARY")
print("Candidate:", name.group(1) if name else "Not found")
print("Email:", email)
print("Mobile:", mobile)
print("Technical Skills:", found)
print("Experience:", years, "years")

if years >= 2 and any(s.lower() == "python" for s in found):
    print("Eligibility: Eligible")
else:
    print("Eligibility: Not Eligible")
