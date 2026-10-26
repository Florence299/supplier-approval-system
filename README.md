# Supplier Approval System
## Project Overview
This project is a Python-based supplier contract approval system that uses predefined business rules to evaluate supplier eligibility and available budget.

The program determines whether a supplier contract should be approved, conditionally approved, or rejected.

## Features

- Checks whether the available budget covers the contract value.
- Evaluates supplier certification and performance rating.
- Checks whether the supplier has recorded violations.
- Determines the appropriate contract approval decision.
- Deducts the contract value from the available budget when approved.
- Generates a low-budget alert when the remaining budget falls below $3,000.

## Approval Rules
Contract Approved: The budget is sufficient, the supplier is certified, and there are no violations.

Conditional Approval: The budget is sufficient, the supplier has a rating of at least 90, and there are no violations, but full approval conditions were not met. 

Contract Rejected: Neither approval condition is satisfied.

## Technologies Used
- Python 3 
- GitHub for version control 

## How to Run 
1. Install Python 3 on your computer. 
2. Download the supplier_approval.py file. 
3. Open a terminal in the folder containing the file.
4. Run the following command:
 'python supplier_approval.py'

## Example Output 
 For the sample values included in the program:
 ```text
  Conditional Approval
  Low Budget Alert
```

## Skills Demonstrated
- Python variables and data types 
- Boolean logic
- Conditional statements
- Comparison operators
- Business rule implementation
- Basic budget management

## Future Improvements
Potential enhancements include user input, evaluating multiple suppliers, storing supplier records, and automated testing. 
 

 
