import yfinance as yf
from ratios import Ratio

# Getting the data. The data was downloaded from Yahoo Finance.

## The data for General Motors
gm = yf.Ticker('GM')
gm_balance_sheet = gm.balance_sheet.T.sort_index(ascending=True)
gm_balance_sheet.index = gm_balance_sheet.index.year
gm_income_statement = gm.income_stmt.T.sort_index(ascending=True)
gm_income_statement.index = gm_income_statement.index.year

## The data for Ford Motors
f = yf.Ticker('F')
f_balance_sheet = f.balance_sheet.T.sort_index(ascending=True)
f_balance_sheet.index = f_balance_sheet.index.year
f_income_statement = f.income_stmt.T.sort_index(ascending=True)
f_income_statement.index = f_income_statement.index.year

# Liquidity ratio including current ratio and quick ratio
current_ratio = Ratio('Current Ratio', 'Current Assets', 'Current Liabilities')
current_ratio.calculate(gm_balance_sheet)
current_ratio.calculate(f_balance_sheet)
current_ratio.draw(gm_balance_sheet, f_balance_sheet)

quick_ratio = Ratio('Quick Ratio', 'Cash And Cash Equivalents', 'Current Liabilities')
quick_ratio.calculate(gm_balance_sheet)
quick_ratio.calculate(f_balance_sheet)
quick_ratio.draw(gm_balance_sheet, f_balance_sheet)

# Debt Ratio is the debt to equity ratio
debt_ratio = Ratio('Debt to Equity', 'Total Debt', 'Stockholders Equity')
debt_ratio.calculate(gm_balance_sheet)
debt_ratio.calculate(f_balance_sheet)
debt_ratio.draw(gm_balance_sheet, f_balance_sheet)

# Efficiency Ratio including inventory turnover ratio
gm_balance_sheet['Average Inventory'] = (gm_balance_sheet['Inventory'] + gm_balance_sheet['Inventory'].shift(1)) / 2
f_balance_sheet['Average Inventory'] = (f_balance_sheet['Inventory'] + f_balance_sheet['Inventory'].shift(1)) / 2

inventory_turnover = Ratio('Inventory Turnover', 'Average Inventory', 'Cost Of Revenue')
inventory_turnover.calculate(f_balance_sheet, f_income_statement)
inventory_turnover.calculate(gm_balance_sheet, gm_income_statement)
inventory_turnover.draw(gm_balance_sheet, f_balance_sheet)

# Profitable Ratio including return on assets and return on equity ratio
roa = Ratio('ROA', 'Net Income', 'Total Assets')
roa.calculate(gm_income_statement, gm_balance_sheet)
roa.calculate(f_income_statement, f_balance_sheet)
roa.draw(gm_income_statement, f_income_statement)

roe = Ratio('ROE', 'Net Income', 'Stockholders Equity')
roe.calculate(gm_income_statement, gm_balance_sheet)
roe.calculate(f_income_statement, f_balance_sheet)
roe.draw(gm_income_statement, f_income_statement)

