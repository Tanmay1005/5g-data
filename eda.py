#%%
import pandas as pd
import matplotlib.pyplot as plt
mobile_data = pd.read_excel('mobile_data.xlsx')
# Filtering data for the specific countries
countries_of_interest = ["United Kingdom", "India", "United States", "Canada", "Germany", "China"]
filtered_data = mobile_data[mobile_data['Name'].isin(countries_of_interest)]

# Creating the bar chart
plt.figure(figsize=(10, 6))
plt.bar(filtered_data['Name'], filtered_data['Average price of 1GB (USD)'], color='skyblue')
plt.title('Average Cost of 1GB Mobile Data (2023)')
plt.xlabel('Country')
plt.ylabel('Average Cost in USD')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# %%
# Saving the filtered data to a CSV file
csv_path = 'filtered_mobile_data.csv'
filtered_data.to_csv(csv_path, index=False)
csv_path
# %%
data_path = 'mobile_data.xlsx'
pd.ExcelFile(data_path).sheet_names

# %%
# Correctly loading the "Historical Data" sheet
historical_data = pd.read_excel(data_path, sheet_name='Historical Data')
historical_data.head()
# %%
# Filtering the historical data for the specific countries
historical_filtered_data = historical_data[historical_data['Name'].isin(countries_of_interest)]

# Extracting relevant columns for the visualization
historical_filtered_data = historical_filtered_data[["Name", "Average price of 1GB (USD – 2019)",
                                                     "Average price of 1GB (USD – 2020)",
                                                     "Average price of 1GB (USD – 2021)",
                                                     "Average price of 1GB (USD – 2022)",
                                                     "Average price of 1GB (USD – 2023)"]]
historical_filtered_data
# %%
# Converting data to numeric for plotting
for year in range(2019, 2024):
    historical_filtered_data[f'Average price of 1GB (USD – {year})'] = pd.to_numeric(historical_filtered_data[f'Average price of 1GB (USD – {year})'], errors='coerce')

# Plotting historical data
plt.figure(figsize=(12, 8))
years = ['2019', '2020', '2021', '2022', '2023']

for index, row in historical_filtered_data.iterrows():
    plt.plot(years, row[1:], marker='o', label=row['Name'])

plt.title('Historical Prices of 1GB Mobile Data (2019-2023)')
plt.xlabel('Year')
plt.ylabel('Average Cost in USD')
plt.legend(title='Country')
plt.grid(True)
plt.show()
# %%
# %%
# Saving the filtered data to a CSV file
csv_path = 'historical_data.csv'
historical_filtered_data.to_csv(csv_path, index=False)
csv_path
# %%
# %%
data_path = 'smartphone5g.xlsx'
pd.ExcelFile(data_path).sheet_names
# %%
# Correctly loading the "Historical Data" sheet
smartphone_data = pd.read_excel(data_path, sheet_name='Data')
# %%
smartphone_data.head()
# %%
smartphone_data.columns
# %%
# %%
data_path = 'smartphone-usa.xlsx'
pd.ExcelFile(data_path).sheet_names
# %%
# Correctly loading the "Historical Data" sheet
smartphone_usa= pd.read_excel(data_path, sheet_name='Data')
# %%
smartphone_usa.head()
# %%
smartphone_usa
# %%
# Directly defining and creating the DataFrame
df_smartphone_ownership = pd.DataFrame({
    "smartphone_yes": [77],
    "smartphone_no": [23]
})
df_smartphone_ownership.loc[1] = [27.4, 72.6] 
# Adding an 'ID' column
df_smartphone_ownership['ID'] = ['usa', 'india'] 
df_smartphone_ownership
# %%
csv_path = 'smartphone_ownership.csv'
df_smartphone_ownership.to_csv(csv_path, index=False)
# %%
import matplotlib.pyplot as plt
import numpy as np

# Labels for the bars
labels = ['Spectrum Acquisition', 'Total 5G Investment']

# Investment data in billions
jio_investments = [11, 24.26]  # in billions USD
airtel_investments = [5.22, 9.09]  # in billions USD

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, jio_investments, width, label='Jio')
rects2 = ax.bar(x + width/2, airtel_investments, width, label='Airtel')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Investment Type')
ax.set_ylabel('Investments in billions USD')
ax.set_title('5G Investments by Jio and Airtel')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
#%%
import csv

# Define the data
headers = ['Company', 'Spectrum Acquisition (billion USD)', 'Total 5G Investment (billion USD)']
data = [
    ['Jio', 11, 24.26],
    ['Airtel', 5.22, 9.09]
]

# Path to save the CSV file
file_path = 'Investments.csv'

# Writing to the CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerow(data[0])
    writer.writerow(data[1])

print(f'Data saved to {file_path}')


# %%
