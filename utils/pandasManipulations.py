import pandas as pd
import datetime

COLUMNHEADER = 'Locations of Dates'

def createdf(tablefile):
    df_dict = pd.read_excel(tablefile, dtype=object, sheet_name=None)
    return df_dict


def datecheckcolumn(df):
    df.insert(len(df.columns), COLUMNHEADER, "")
    return df


def listdatelocations(df):
    df_copy = df.applymap(lambda x: x if isinstance(x, datetime.date) is True else "")

    for index, row in df_copy.iterrows():
        col_list = [c for c in row.index.to_list() if row.loc[c] != ""]
        df.at[index, COLUMNHEADER] = str(col_list)
    return df


def highlight_color(series):
    '''
    highlight the maximum in a Series yellow.
    '''
    is_date = [v if isinstance(v, datetime.date) is True else '' for v in series]
    return ['background-color: yellow' if v else '' for v in is_date]


def highlightdates(df):
    df_styled = df.style.apply(highlight_color)
    return df_styled

