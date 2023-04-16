import pandas as pd


def clean_date(dta_df):
    """
    Tansform date column to pandas date object and eliminate
    rows with anormal value
    
    Inputs:
        dta_df: a pd.DataFrame
    """
    
    wrong_date = dta_df['date'].map(len) != 10
    dta_df.drop(index=dta_df[wrong_date].index, inplace=True)


def import_csv(filepath):
    """
    Import csv file as pd.DataFrame 
    
    Inputs:
        filepath: the path of the data
    Outputs:
        dta_df: a pd.DataFrame
    """
    
    assert filepath.endswith('.csv'), "Wrong file format !"
    
    dta_df = pd.read_csv(filepath, encoding="utf_8_sig", lineterminator='\n')
    
    return dta_df


def clean(filepath):
    """
    Clean the input data and export the data
    """
    
    assert filepath.endswith('.csv'), 'Must be .csv file !'

    dta_df = import_csv(filepath)
    clean_date(dta_df)
    dta_df.dropna(inplace=True)
    dta_df.reset_index(inplace=True, drop=True)
    
    return dta_df
