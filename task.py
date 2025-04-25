import pandas as pd

# Indexing Tasks:
df = pd.read_csv('sales-feb-2015.csv', parse_dates=['Date'], index_col='Date')
print("Data loaded with 'Date' as index:\n", df.head(), "\n")

units_1 = df['Units']['2015-02-05 02:00:00']
units_2 = df.loc['2015-02-05 02:00:00', 'Units']
print("Units using square brackets:", units_1)
print("   Units using .loc:", units_2, "\n")

df_company_units = df[['Company', 'Units']]
print("Company and Units DataFrame:\n", df_company_units.head(), "\n")

# Slicing Tasks:
df_feb3_to_5 = df['2015-02-03':'2015-02-05']
print("Sales from Feb 3 to Feb 5:\n", df_feb3_to_5, "\n")

df_first_5 = df[:5]
print("First 5 entries:\n", df_first_5, "\n")

df_hooli = df.loc[df['Company'] == 'Hooli']
print("All Hooli entries:\n", df_hooli.head(), "\n")

df_iloc = df.iloc[2:5, 1:3]
print("iloc rows 2-4, columns 1-2:\n", df_iloc, "\n")

# Filtering Tasks:
df_units_gt10 = df[df['Units'] > 10]
print("Entries with >10 units sold:\n", df_units_gt10.head(), "\n")

mask_software = df['Product'] == 'Software'
df_software = df[mask_software]
print("Software product sales:\n", df_software.head(), "\n")

df_hw_or_gt15 = df[(df['Product'] == 'Hardware') | (df['Units'] > 15)]
print("Hardware or >15 units:\n", df_hw_or_gt15.head(), "\n")

df_no_nan = df.dropna()
print("DataFrame without NaNs:\n", df_no_nan.head(), "\n")

# Transforming Tasks:
price_map = {'Software': 350, 'Hardware': 425, 'Service': 275}
df['Revenue'] = df['Units'] * df['Product'].map(price_map)
print("DataFrame with Revenue:\n", df[['Product', 'Units', 'Revenue']].head(), "\n")

df['DayOfWeek'] = df.index.day_name()
print("Day of week column:\n", df[['DayOfWeek']].head(), "\n")

df['Revenue'] = df.apply(lambda x: x['Revenue'] * 0.9 if x['Units'] >= 20 else x['Revenue'] * 0.95 if x['Units'] >= 15 else x['Revenue'], axis=1)
print("Revenue after discounts:\n", df[['Units', 'Revenue']].head(), "\n")

df['CompanyCode'] = df['Company'].str.upper().str[:3]
print("CompanyCode column:\n", df[['Company', 'CompanyCode']].head(), "\n")
