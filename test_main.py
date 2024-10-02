# from main import present_value
from main import present_value


def test_add():
    # Test 1: Empty cash flow dictionary
    assert present_value({}, 0.04) == "Current dictionary has no Cash Flow Data"

    # Test 2: Cash flow all in the current year
    cash_flow = {2024: 1000}
    assert present_value(cash_flow, 0.04) == 1000

    # Test 3: Cash flow in future years
    cash_flow = {2025: 1000, 2026: 2000}
    expected_value = 1000 / (1.04) + 2000 / (1.04**2)
    assert abs(present_value(cash_flow, 0.04) - expected_value) < 1e-6


if __name__ == "__main__":
    test_add()
    print("Test Complete & passed!")


# def test_present_value():
#     "Testing Out a fucntion"
#     assert present_value({2024: 10000}, 0.00) == 10000
#     assert present_value({}, 0.00) == "Current data structure has has no Cash Flow Info"


# from main import add


# def test_add():
#     assert add(2, 2) == 4
#     assert add(1, 2) == 3
#     assert add(1, 1) == 2
