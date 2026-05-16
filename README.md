
# Youth Unemployment and Inflation Analysis in Europe

## Project Overview

This project analyzes the relationship between youth unemployment and inflation rates across European countries using World Bank data for 2024.

The project uses Python for:
- data cleaning,
- data merging,
- visualization,
- and statistical analysis.


## Objectives

- Explore whether inflation and youth unemployment are related
- Visualize macroeconomic patterns across countries
- Apply statistical methods to real-world economic data


## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

## Dataset Sources

Data obtained from:
- World Bank Data

Indicators used:
- Youth unemployment rate (ages 15–24)
- Inflation, consumer prices (annual %)

## Methods

1. Loaded CSV datasets
2. Cleaned and filtered relevant columns
3. Merged datasets by country
4. Removed missing values
5. Calculated correlation
6. Applied linear regression
7. Created visualization with regression line


## Results

The correlation between inflation and youth unemployment was approximately:

-0.03

This suggests there was little to no linear relationship between inflation and youth unemployment in the selected 2024 dataset.


## Visualization

The generated graph is saved in the `images/` folder.


## How to Run

Install dependencies:

```bash
pip install pandas matplotlib scikit-learn
```

Run the project:

```bash
python analysis.py
```


## Project Structure

```text
youth-unemployment-europe-analysis/
│
├── data/
├── images/
├── notebooks/
├── analysis.py
├── requirements.txt
└── README.md
```
## Multiple Regression Results

A multiple regression model was estimated using:
- inflation rates,
- and GDP growth rates

to predict youth unemployment.

Results suggested:
- inflation had little relationship with unemployment,
- while higher GDP growth was associated with lower youth unemployment.

The GDP growth coefficient was approximately -0.82, indicating a stronger macroeconomic relationship.
