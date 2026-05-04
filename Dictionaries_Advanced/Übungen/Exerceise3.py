"""Exercise 3 — Nested Dictionary Access
Given this data:
company = {
    "engineering": {
        "headcount": 45,
        "budget": 500000,
        "lead": "Sarah"
    },
    "marketing": {
        "headcount": 12,
        "budget": 200000,
        "lead": "James"
    },
    "support": {
        "headcount": 20,
        "budget": 150000,
        "lead": "Elena"
    }
}
Write code that:

Prints the lead of the engineering department
Prints the total headcount across all departments
Prints the name of the department with the highest budge"""


company = {
    "engineering": {
        "headcount": 45,
        "budget": 500000,
        "lead": "Sarah"
    },
    "marketing": {
        "headcount": 12,
        "budget": 200000,
        "lead": "James"
    },
    "support": {
        "headcount": 20,
        "budget": 150000,
        "lead": "Elena"
    }
}


print(company["engineering"]["lead"])
total_headcount = sum(dept["headcount"]for dept in company.values())
print(f"Toatal headcount: {total_headcount}")

def get_budget(dept_name):
    return company[dept_name]["budget"]

highest_budget_dept = max(company, key=get_budget)
print(f"Abteilung mit dem hochstem Budget ist: {highest_budget_dept}")




