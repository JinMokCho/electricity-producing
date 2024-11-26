import pandas as pd

df = pd.read_excel("C:\data.xlsx")

# Assuming you have a DataFrame called 'df' with a column named 'Energy Source'
electricity_supplied_count = df['PRODUCT'].value_counts()['Electricity supplied']

net_electricity_production_count = df['PRODUCT'].value_counts()['Net electricity production']
final_consumption_count = df['PRODUCT'].value_counts()['Final consumption']
Total_combustible_fuels_count = df['PRODUCT'].value_counts()['Total combustible fuels']

print("electricity production:", net_electricity_production_count)
print("Final consumption:", final_consumption_count)
print("Electricity supplied:", electricity_supplied_count)
print("Total combustible fuels:", Total_combustible_fuels_count)
