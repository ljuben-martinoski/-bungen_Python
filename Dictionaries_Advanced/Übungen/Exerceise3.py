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
print(company["marketing"]["engineering"]["support"]["headcount"][sum])
print(company["support"])

