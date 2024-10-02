# import math


# def add(x, y):
#     return math.ceil(x) + math.floor(y)


from datetime import datetime


def present_value(cash_flow, discount_rate=0.04):
    if not cash_flow:
        return "Current dictionary has no Cash Flow Data"

    current_year = datetime.now().year
    present_val = 0

    for year, amount in cash_flow.items():
        if year < current_year:
            continue

        n = year - current_year
        present_val += amount / ((1 + discount_rate) ** n)

    return present_val


# # Test Cases
# cs_1 = {1999: 10193210,  2027: 23450, 2030: 678819} # Test case including date in the past
# cs_2 = {} # Test Case Including Blank
# cs_3  = {2024: 2300, 2025: 91021, 2026: 34599, 2030: 56660} #Normal Test Case
# cs_4 = {2024: 2300, 2025: 91021, 2026: 34599.17} #Test Case Including Decimal
