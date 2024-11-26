'''
import pandas as pd


# Load the Excel file into a Pandas DataFrame
df = pd.read_excel("C:\data.xlsx")

# Display the contents of the DataFrame
print(df['share'].describe())
'''


# 컬럼에 있는 값 출력, 중복값은 1회만 출력
import pandas as pd

# Load your dataset that contains the "country" column
data = pd.read_excel('C:\data.xlsx')

# Get unique values in the "country" column
unique_countries = data['COUNTRY'].unique()

# Print the unique country values
print(unique_countries)


'''
#국가를 대륙으로 그룹화
import pandas as pd

# Load the Excel file into a Pandas DataFrame
data = pd.read_excel("C:\data.xlsx")

# Create a DataFrame with the country column
data = pd.DataFrame({'COUNTRY':['Australia' 'Austria' 'Belgium' 'Canada' 'Chile' 'Czech Republic'
 'Denmark' 'Estonia' 'Finland' 'France' 'Germany' 'Greece' 'Hungary'
 'IEA Total' 'Iceland' 'Ireland' 'Italy' 'Japan' 'Korea' 'Latvia'
 'Lithuania' 'Luxembourg' 'Mexico' 'Netherlands' 'New Zealand' 'Norway'
 'OECD Americas' 'OECD Asia Oceania' 'OECD Europe' 'OECD Total' 'Poland'
 'Portugal' 'Republic of Turkiye' 'Slovak Republic' 'Slovenia' 'Spain'
 'Sweden' 'Switzerland' 'United Kingdom' 'United States' 'Colombia'
 'Argentina' 'Brazil' 'Bulgaria' 'Croatia' 'Cyprus' 'India' 'Malta'
 'North Macedonia' 'Romania' 'Serbia' 'Costa Rica']})

# Create a dictionary mapping each country to its corresponding continent
continent_mapping = {
    'Australia': 'Australia',
    'Austria': 'Europe',
    'Belgium': 'Europe',
    'Canada': 'North America',
    'Chile': 'South America',
    'Czech Republic': 'Europe',
    'Denmark': 'Europe',
    'Estonia': 'Europe',
    'Finland': 'Europe',
    'France': 'Europe',
    'Germany': 'Europe',
    'Greece': 'Europe',
    'Hungary': 'Europe',
    'IEA Total': 'IEA',
    'Iceland': 'Europe',
    'Ireland': 'Europe',
    'Italy': 'Europe',
    'Japan': 'Asia',
    'Korea': 'Asia',
    'Latvia': 'Europe',
    'Lithuania': 'Europe',
    'Luxembourg': 'Europe',
    'Mexico': 'North America',
    'Netherlands': 'Europe',
    'New Zealand': 'Oceania',
    'Norway': 'Europe',
    'OECD Americas': 'OECD',
    'OECD Asia Oceania': 'OECD',
    'OECD Europe': 'OECD',
    'OECD Total': 'OECD',
    'Poland': 'Europe',
    'Portugal': 'Europe',
    'Republic of Turkey': 'Europe',
    'Slovak Republic': 'Europe',
    'Slovenia': 'Europe',
    'Spain': 'Europe',
    'Sweden': 'Europe',
    'Switzerland': 'Europe',
    'United Kingdom': 'Europe',
    'United States': 'North America',
    'Colombia': 'South America',
    'Argentina': 'South America',
    'Brazil': 'South America',
    'Bulgaria': 'Europe',
    'Croatia': 'Europe',
    'Cyprus': 'Europe',
    'India': 'Asia',
    'Malta': 'Europe',
    'North Macedonia': 'Europe',
    'Romania': 'Europe',
    'Serbia': 'Europe',
    'Costa Rica': 'Central America'
}

# Use the map function to create the Continent column based on the country column
data['Continent'] = data['COUNTRY'].map(continent_mapping)

# Print the resulting DataFrame
print(data)
'''

'''
#국가를 대륙으로 분류
import pandas as pd

# Define the mapping table that associates countries with continents
mapping_table = pd.DataFrame({
    'country': ['Australia', 'Austria', 'Belgium', 'Canada', 'Chile', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'IEA Total', 'Iceland', 'Ireland', 'Italy', 'Japan', 'Korea', 'Latvia', 'Lithuania', 'Luxembourg', 'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'OECD Americas', 'OECD Asia Oceania', 'OECD Europe', 'OECD Total', 'Poland', 'Portugal', 'Republic of Turkey', 'Slovak Republic', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'United Kingdom', 'United States', 'Colombia', 'Argentina', 'Brazil', 'Bulgaria', 'Croatia', 'Cyprus', 'India', 'Malta', 'North Macedonia', 'Romania', 'Serbia', 'Costa Rica'],
    'continent': ['Australia', 'Europe', 'Europe', 'North America', 'South America', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'IEA', 'Europe', 'Europe', 'Europe', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'North America', 'Europe', 'Oceania', 'Europe', 'OECD', 'OECD', 'OECD', 'OECD', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'North America', 'South America', 'South America', 'Europe', 'Europe', 'Europe', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'Central America']
})

# Sort the countries by continent
sorted_countries = mapping_table.sort_values('continent')

print(sorted_countries)
'''

'''
# 새로운 컬럼을 만들고 그룹화
import pandas as pd

# Define the mapping dictionary that associates countries with continents
continent_mapping = {
    'Australia': 'Australia',
    'Austria': 'Europe',
    'Belgium': 'Europe',
    'Canada': 'North America',
    'Chile': 'South America',
    'Czech Republic': 'Europe',
    'Denmark': 'Europe',
    'Estonia': 'Europe',
    'Finland': 'Europe',
    'France': 'Europe',
    'Germany': 'Europe',
    'Greece': 'Europe',
    'Hungary': 'Europe',
    'IEA Total': 'IEA',
    'Iceland': 'Europe',
    'Ireland': 'Europe',
    'Italy': 'Europe',
    'Japan': 'Asia',
    'Korea': 'Asia',
    'Latvia': 'Europe',
    'Lithuania': 'Europe',
    'Luxembourg': 'Europe',
    'Mexico': 'North America',
    'Netherlands': 'Europe',
    'New Zealand': 'Oceania',
    'Norway': 'Europe',
    'OECD Americas': 'OECD',
    'OECD Asia Oceania': 'OECD',
    'OECD Europe': 'OECD',
    'OECD Total': 'OECD',
    'Poland': 'Europe',
    'Portugal': 'Europe',
    'Republic of Turkey': 'Europe',
    'Slovak Republic': 'Europe',
    'Slovenia': 'Europe',
    'Spain': 'Europe',
    'Sweden': 'Europe',
    'Switzerland': 'Europe',
    'United Kingdom': 'Europe',
    'United States': 'North America',
    'Colombia': 'South America',
    'Argentina': 'South America',
    'Brazil': 'South America',
    'Bulgaria': 'Europe',
    'Croatia': 'Europe',
    'Cyprus': 'Europe',
    'India': 'Asia',
    'Malta': 'Europe',
    'North Macedonia': 'Europe',
    'Romania': 'Europe',
    'Serbia': 'Europe',
    'Costa Rica': 'Central America'
}

# Load your dataset that contains the "country" column
# Load the Excel file into a Pandas DataFrame
data = pd.read_excel("C:\data.xlsx")

# Create a new column "continent" by mapping the countries to continents
data['continent'] = data['COUNTRY'].map(continent_mapping)

# Sort the data by continent
#sorted_data = data.sort_values('continent')

# Assuming your data is stored in a DataFrame called "df"
data.dropna(subset=['previousYearToDate'], inplace=True)

print(data)

data.to_excel('continent_mapping.xlsx', index=False)
'''

'''
# previousYearToDate 컬럼 중 null 값인 데이터 삭제
import pandas as pd

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel("C:\data.xlsx")

# Assuming your data is stored in a DataFrame called "df"
df.dropna(subset=['previousYearToDate'], inplace=True)

print(df)
'''








