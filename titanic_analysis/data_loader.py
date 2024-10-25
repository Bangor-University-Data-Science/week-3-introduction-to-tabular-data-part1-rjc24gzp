import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
 
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        raise
    except pd.errors.EmptyDataError:
        print(f"The file {filepath} is empty.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise