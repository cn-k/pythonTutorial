import pandas as pd
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)
txt_df = pd.read_csv("files/supermarkets/supermarkets-semi-colons.txt", sep=";")
print(txt_df)