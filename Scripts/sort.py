import pandas as pd
import glob

file_path = glob.glob(r'\Path\to\file\to be sorted.xlsx')
Dump = ''.join(file_path)

df1 = pd.read_excel(r'\Path\to\master list.xlsx', sheet_name='Sheet1', usecols='A')
df1 = df1.sort_values("A")
df1 = df1.fillna(0)
df1 = df1[df1['A'] != 0]
df2 = pd.read_excel(Dump, sheet_name='Sheet1', usecols='C')
df2 = df2.drop_duplicates("C")
df2 = df2.sort_values("C")
df2 = df2.fillna(0)

with pd.ExcelWriter("Sorted_file.xlsx", mode="a", if_sheet_exists="overlay") as writer:
    df1.to_excel(writer,sheet_name="Sheet1", columns=["A"], index=False)
    df2.to_excel(writer, sheet_name="Sheet1", columns=["C"], startcol=1, index=False)


print(df1)
print(df2)
