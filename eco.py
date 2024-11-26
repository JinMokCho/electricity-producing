import pandas as pd

df = pd.read_excel("C:\Eco_Classification_go.xlsx")

# PRODUCT 칼럼 내 데이터 조회
'''
# Get unique values in the "country" column
unique_PRODUCT = df['PRODUCT'].unique()

# Print the unique country values
print(unique_PRODUCT)
'''


# List of eco-friendly production methods
eco_friendly_methods = ['Hydro', 'Wind', 'Solar', 'Geothermal', 'Natural gas', 'Renewables', 'Other renewables aggregated', 'Other renewables', 'Low carbon', 'Combustible renewables']

# Create a new column 'Environmental Classification' and assign 'Eco-Friendly' or 'Non-Environmental' based on the 'PRODUCT'
df['Environmental Classification'] = df['PRODUCT'].apply(lambda x: 'Eco-Friendly' if x in eco_friendly_methods else 'Non-Environmental')

# Print the updated DataFrame
print(df)

df.to_excel('Eco_Classification_real_end.xlsx', index=False)










