from typing import DefaultDict
import pandas as pd

# Create a key:value collection of series to use
# to populate the dataframe for testing
data = {'Month':pd.Series(['January','February','March','April','May',
'June','July','August','September','October','November','Decemeber']),
    'Rainfall':pd.Series([1.65,1.25,1.94,2.75,2.75,3.65,5.05,
    1.50,1.33,0.07,0.50,2.30]),
    }


# Create a DataFrame using the static data
df = pd.read_json(r'./rain.json')

print("Our data frame:")
print(df, "\n")

# Remove rows with missing values
dfclean = df.dropna()

print("Our data frame with dropped values: \n", dfclean)

# Create a count of all rows that contain NaNs
count = 0
for index, row in df.iterrows():
    if any(row.isnull()):
        count = count + 1
print("\n Number of rows with NaNs: "+ str(count))

# Calculate average rainfall and temperature
print("Average rainfall and temperature:")
print(dfclean[['Rainfall']].mean())
print(dfclean[['Temperature']].mean())

# Calculate median rainfall and temperature
print("\n Median:")
print(dfclean[['Rainfall']].median())
print(dfclean[['Temperature']].median())

# Calculate standard deviation rainfall and temperature
print("\n Standard Deviation:")
print(dfclean[['Rainfall']].std())
print(dfclean[['Temperature']].std(), '\n')

# Print the rainfall and mean for first few months
rainfall = dfclean['Rainfall'][0:3]
print(rainfall,'\n')
print("Average rainfall in the first three months:",rainfall.mean(), '\n')

print("\n Just temperature and rainfall data")
dfTempRain = (dfclean[['Temperature','Rainfall']])
print(dfTempRain)
print('\n' "Mean: ")
print(dfTempRain.mean())

index = dfclean['Month']
dfIndexed = dfclean.set_index(index)

# Require a properly indexed dataframe
print("Find a row by value \n", dfIndexed.loc['March'])