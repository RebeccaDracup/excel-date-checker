# import openpyxl
from pathlib import Path
import re
import pandas as pd


def exporttoexcel(df_dict_formatted, tablefilepath, sheetnames):
    filepath = re.sub(r"\.xlsx", "_dates.xlsx", tablefilepath)
    writer = pd.ExcelWriter(Path(filepath), engine='xlsxwriter')
    for sheetname in sheetnames:
        df_dict_formatted.get(sheetname).to_excel(writer, sheet_name=sheetname)
    writer.save()
