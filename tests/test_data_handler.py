from src.data_handler import clean_data, remove_iqr_outliers
import pandas as pd
import numpy as np

# Test clean_data for removing duplicated rows 
def test_clean_data_remove_duplicates():
    df = pd.DataFrame({'A': [1, 1, 2], 'B': [3, 3, 5]})
    cleaned = clean_data(df)
    assert len(cleaned) == 2  

# Test clean_data for removing NaN values
def test_clean_data_remove_empty_cells():
    df = pd.DataFrame({'A': [1, 4, 2], 'B': [3, 3, np.nan]})
    cleaned = clean_data(df)
    assert cleaned['B'].isna().sum() == 0  

# Test remove_outliers for removing extreme values
def test_remove_outliers(sample_data):
    sample_data.loc[0, 'Daily_Usage_Hours'] = 1000 
    cleaned = remove_iqr_outliers(sample_data, ['Daily_Usage_Hours'])
    assert len(cleaned) < len(sample_data)
    assert cleaned['Daily_Usage_Hours'].max() < 1000