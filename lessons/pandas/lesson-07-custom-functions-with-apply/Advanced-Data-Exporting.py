import pandas as pd
import numpy as np

# Creating a sample DataFrame
df = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100))
})

# Exporting to Excel with multiple sheets
with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Sheet1')
    df.to_excel(writer, sheet_name='Sheet2')

    # Accessing the XlsxWriter workbook and worksheet objects
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Adding a format
    format = workbook.add_format({'num_format': '#,##0'})
    worksheet.set_column('B:B', None, format)