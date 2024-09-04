# General Motors and Ford Motors Financial Analysis 2021-2023

The purpose of this project is to examine wheather the investors should invest in
General Motors or Ford Motors. The method used is the financial ratio analysis 
including liquidity, debts, efficiency, and profitability ratios. The data was downloaded
from the Yahoo Finance website (available at: https://finance.yahoo.com/). The project was conducted
by Python 3.10.4.

## Project structure
The project is organized as follows:

- 'README.md': The project description.
- 'main.py': The main Python script to run the application.
- 'ratios.py': This file contains a class and several functions for data calculation and visualization.
- Images: The graph showing the trend of each ratio saved in this directory.
- 'Analysis.md': An analysis of each type of financial ratio and the conclusion.
- 'requirements.txt': Contains the list of dependencies.

# Functionalities
### Calculating Financial Ratio
Each ratio was calculated by:
- First, initiate the class `Function`. 
```commandline
current_ratio = Function('Current Ratio', 'Current Assets', 'Current Liabilities')
```
- Second, call the function `xxx` to calculate the desired ratio
```commandline
current_ratio.caculate1(gm_balance_sheet)
current_ratio.caculate1(f_balance_sheet)
```

### Plotting graph

# Summary
