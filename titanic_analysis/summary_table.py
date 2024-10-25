import pandas as pd

def create_summary_table(df: pd.DataFrame) -> pd.DataFrame:
    
    summary = pd.DataFrame({
        'Feature Name': df.columns,
        'Data Type': df.dtypes,
        'Number of Unique Values': [df[col].nunique() for col in df.columns],
        'Has Missing Values?': [df[col].isnull().any() for col in df.columns]  
    })
   
    return summary