# chris_moreira_mini_project_IDS720

[![CI by Chris](https://github.com/nogibjj/chris_moreira_mini_project_IDS706/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/chris_moreira_mini_project_IDS706/actions/workflows/hello.yml)


Cash Flow Calculator

Input 
1. A dictionary of future cash flows in the form {2025: 10000, 2026: 30000, 2029: 3000} where each key represents a future year and each value represents a dollar amount expected that ueat 
2. Discount rate: this is a fundamental input in the disocunted cash flow formula. Basically it assess the potential return on an investment that is risk free. Typically this will be yield of a 10yr US treasure bond -- today being around 4%

Output
Present Value of future cash flows. 
Here we use the formula for present value: 
PV = CF / (1+r)^t 
CF -> Cash flow that year
t -> difference of future year to current year
r -> Discount Rate
PV -> our variable of interest (present value)

What are some of our data requirements:
- We don't return a PV when there's no data, instead we simply state cash flow data does not exist
- We exclude cash flow from the past. i.e. if we have a cash flow dictionary in the form {2020: 100000, 2024: 100000} we would exclude 2020 since that year was in the past. 
