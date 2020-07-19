import pandas as pd
import numpy as np

# Read data
my_dataframe = pd.read_excel('full_export.xlsx')

# Find duplicates
duplicatesDF = my_dataframe[my_dataframe.duplicated(
    ['First Name', 'Last Name'])]
print(duplicatesDF)
# Output to xlsx
