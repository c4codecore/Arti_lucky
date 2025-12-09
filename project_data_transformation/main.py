import pandas as pd
import numpy as np

# 1. Read all data without a header to inspect and construct the two-level header
df_all = pd.read_excel("input.xlsx", header=None)

# 2. Extract header rows (R3 is index 2, R4 is index 3)
r3 = df_all.iloc[2]
r4 = df_all.iloc[3]

# 3. Prepare the combined header (indices 3 to 10)
# Forward fill R3 to spread the 'Above Function' name
r3_filled = r3.iloc[3:11].ffill()

# Combine R3 (Above Function) and R4 (Attribute)
combined_headers = (r3_filled + '_' + r4.iloc[3:11]).tolist()

# 4. Construct the full list of new column names
new_columns = ['col_to_drop_0', 'Function', 'col_to_drop_2'] + combined_headers
# Check if there is a column 11 and append a name if so
if df_all.shape[1] > len(new_columns):
    new_columns.append('col_to_drop_11')

# 5. Create a new DataFrame using the original data from row 5 onwards (index 5)
df = df_all.iloc[5:].copy()
df.columns = new_columns

# Drop auxiliary columns
df = df.drop(columns=['col_to_drop_0', 'col_to_drop_2', 'col_to_drop_11'], errors='ignore')

# 6. Melt the DataFrame to unpivot the data
df_long = df.melt(
    id_vars=['Function'],
    var_name='Combined_Attribute',
    value_name='Value'
).dropna(subset=['Value']) # Drop rows where the email/Value is NaN

# 7. Split the 'Combined_Attribute' into 'Above Function' and 'Attribute'
df_long[['Above Function', 'Attribute']] = df_long['Combined_Attribute'].str.split('_', n=1, expand=True)

# 8. Explode the 'Value' column to handle multiple semicolon-separated emails
# Clean up value string, split by ';', and then explode
df_long['Value'] = df_long['Value'].str.replace(' ', '', regex=False).str.split(';')
df_exploded = df_long.explode('Value').reset_index(drop=True)

# Final cleanup of email values and removing empty rows
df_exploded['Value'] = df_exploded['Value'].str.strip()
df_exploded = df_exploded.dropna(subset=['Value'])
df_exploded = df_exploded[df_exploded['Value'] != '']

# 9. Add constant columns: 'Zone' and 'Country'
df_exploded['Zone'] = 'AOA'
df_exploded['Country'] = 'Thailand'

# 10. Select and reorder columns to match the desired output format
final_df = df_exploded[[
    'Zone',
    'Country',
    'Function',
    'Value',
    'Attribute',
    'Above Function'
]]

# Write the result to a new CSV file
output_file_name = 'transformed_output.csv'
final_df.to_csv(output_file_name, index=False)