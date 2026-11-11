# Python Sales Analysis Project

## Project Overview
This project analyzes department-wise sales target and achievement data using Python. It calculates performance gaps and achievement percentages to understand department performance.

## Tools & Technologies
- Python
- Pandas
- Matplotlib
- Excel

## Dataset
The dataset contains department-wise information:
- Department Name
- Sum of Target
- Sum of Achieved

## Analysis Performed
1. Imported Excel data using Pandas.
2. Displayed dataset structure and column names.
3. Removed the Grand Total row for department-level analysis.
4. Calculated the performance gap between Target and Achieved.
5. Calculated Achievement Percentage.
6. Created a Department Achievement Percentage chart.
7. Created a Target vs Achieved comparison chart.

## Key Results

| Department | Target | Achieved | Gap | Achievement |
|---|---:|---:|---:|---:|
| HR | 60,000 | 59,000 | 1,000 | 98.33% |
| IT | 180,000 | 175,000 | 5,000 | 97.22% |
| Sales | 185,000 | 182,000 | 3,000 | 98.38% |

## Project Files
- `sales_analysis.py` – Python analysis code
- `raw data.xlsx` – Input dataset
- `department_target_vs_achieved.png` – Target vs Achieved chart

## How to Run

Install required libraries:

```bash
pip install pandas matplotlib openpyxl
```

Run the Python file:

```bash
python sales_analysis.py
```

## Learning Outcomes
- Excel data handling using Python
- Data cleaning and transformation
- Basic data analysis
- Data visualization using Matplotlib

## Author
Nagesh Kamble

GitHub: https://github.com/Nageshhh0311
