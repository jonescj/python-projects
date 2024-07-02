import pandas as pd

from pandas.tseries.offsets import CustomBusinessDay
import pandas as pd

# Define custom business days
weekmask = 'Mon Tue Wed Thu'
holidays = ['2023-12-25', '2023-12-26']
custom_bday = CustomBusinessDay(weekmask=weekmask, holidays=holidays)

# Create a date range with custom business days
date_range = pd.date_range(start='2023-12-01', periods=10, freq=custom_bday)
print(date_range)

df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Value': range(10)
})

# Shifting dates
df['Shifted'] = df['Date'] + pd.DateOffset(days=2)
print(df)