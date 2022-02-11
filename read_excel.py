import pandas as pd
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)
excel_df = pd.read_excel("files/supermarkets/supermarkets.xlsx", sheet_name=0)
print(excel_df)