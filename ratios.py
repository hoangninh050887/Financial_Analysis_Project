import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

class Function:

    def __init__(self, ratio1, element_1, element_2):
        self.ratio = ratio1
        self.element1 = element_1
        self.element2 = element_2

    # Define function to for calculating ratios which take data from balance sheet only
    def caculate1(self, data):
        data[self.ratio] = data[self.element1] / data[self.element2]
        return data[self.ratio]

    # Define a function for calculating ratios which take data from both balance sheet and income statement
    def caculate2(self, data1, data2):
        data1[self.ratio] = data1[self.element1] / data2[self.element2]
        return data1[self.ratio]

    # The function used for drawing the ratio values
    def draw(self, data1, data2):
        # Data for plotting
        years = np.array(data1.tail(3).index)
        gm = data1[self.ratio].tail(3).astype(float)
        f = data2[self.ratio].tail(3).astype(float)

        # Linear regression for trend lines. The trend lines present the variation trend of the ratios
        gm_fit = np.polyfit(years, gm, 1)
        f_fit = np.polyfit(years, f, 1)
        gm_trend = np.polyval(gm_fit, years)
        f_trend = np.polyval(f_fit, years)

        # Calculating the data that relates to the trend line
        slope_gm, intercept_gm, r_value_gm, p_value_gm, std_err_gm = linregress(years, gm)
        slope_f, intercept_f, r_value_f, p_value_f, std_err_f = linregress(years, f)
        r_squared_gm = r_value_gm ** 2
        r_squared_f = r_value_f ** 2

        # Plotting the data
        plt.figure(figsize=(10, 6))
        plt.plot(years, gm, label='General Motors', marker='o', color='blue')
        plt.plot(years, f,  label='Ford Motors', marker='o', color='orange')

        # Plotting the trend lines
        plt.plot(years, gm_trend,
                 label=f"y={slope_gm.round(3)}x + {intercept_gm.round(2)}\nR2: {r_squared_gm.round(2)}"
                 , linestyle='--', color='blue', alpha=0.7)
        plt.plot(years, f_trend,
                 label=f"y={slope_f.round(3)}x + {intercept_f.round(2)}\nR2: {r_squared_f.round(2)}",
                 linestyle='--', color='orange', alpha=0.7)

        # Adding labels and title
        plt.title(self.ratio)
        plt.xlabel('Year')
        plt.ylabel(f"{self.ratio}={self.element1}/{self.element2}")
        plt.legend()
        plt.grid(True)

        # save the graph
        plt.savefig(os.path.join('Images', f'{self.ratio}.png'))

        # Display the plot
        plt.show()
