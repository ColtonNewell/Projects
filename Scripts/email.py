import pandas as pd
import win32com.client as win32
from datetime import datetime
import os

df3 = pd.read_excel('Sorted_file.xlsx', sheet_name='Sheet1', usecols="C,D")
df3 = df3.fillna(0)
df3 = df3[df3['D'] != 0]
df3 = df3.sort_values("D", kind='stable')

df4 = pd.read_excel('Sorted_file.xlsx', sheet_name='Sheet1', usecols="C")
df4 = df4.fillna(0)
df4 = df4[df4['C'] != 0]
df4 = df4.sort_values("C", kind='stable')
print(df4)
with pd.ExcelWriter("Master list.xlsx", mode="a", if_sheet_exists="overlay") as masterwriter:
    df4.to_excel(masterwriter, sheet_name="Sheet1", columns=["C"], startrow=masterwriter.sheets["Sheet1"].max_row, header=False, index=False)

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

mail.Subject = 'New Names for Training'
mail.To = "myemail@email.com"
mail.HTMLBody = r"""
Hello,<br><br>
Here are the names of the employees to be enrolled in the new training:<br><br>
{0}<br>
Thank you,<br>
Colton Newell<br>
""".format(df3.to_html(index=False))
mail.Save()

