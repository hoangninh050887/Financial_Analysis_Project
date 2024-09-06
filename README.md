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
- 'ratios.py': This file contains a class and functions for data calculation and visualization.
- Images: The graph showing the trend of each ratio saved in this directory.
- 'Analysis.md': An analysis of each type of financial ratio and the conclusion.
- 'requirements.txt': Contains the list of dependencies.

# Functionalities
- First, initiate the class `Ratio`; this class has three input data including the name of a ratio and two elements 
for computing it. These data will be used for calculating and drawing by two functions of the `Ratio` class.
```commandline
current_ratio = Ratio('Current Ratio', 'Current Assets', 'Current Liabilities')
```
### Calculating Financial Ratio

- The function `calculate` is called to calculate the desired ratio. The `calculate` function take the data from the 
balance sheet or the income statement of each company. In this project each ratio is computed twice, one for General 
Motors and one for Ford Motors.
- After calculating, the ratio of each company is added to its balance sheet.
```commandline
current_ratio.caculate(gm_balance_sheet)
current_ratio.caculate(f_balance_sheet)
```
### Plotting graph
- The function `draw` is called for plotting the value of each ratio. The `draw` function take data from the balance
sheet of General Motors and Ford Motors.
```commandline
current_ratio.draw(gm_balance_sheet, f_balance_sheet)
```
- This is an example of a graph that demonstrates the value of current ratio of both firms:
![Current Ratio](./Images/Current%20Ratio.png)

