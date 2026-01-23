import pandas as pd
import logging

# Load the data from CSV file
def load_csv(path):
    try:
        logging.info(f"Loading dataset from {path}")
        data = pd.read_csv(path)
        logging.info(f"Dataset loaded: {data.shape[0]} rows, {data.shape[1]} columns")
        return data
    except:
        logging.error(f"Error loading file {path}")

# Clean the dataset from duplicates
def remove_duplicates(data):
    clean_data = data.drop_duplicates()
    logging.info(f"Data cleaned. New size: {data.shape[0]} rows, {data.shape[1]} columns")
    return clean_data

# Clean the dataset from empty cells
def remove_empty_cells(data):
    clean_data = data.dropna()
    logging.info(f"Data cleaned. New size: {data.shape[0]} rows, {data.shape[1]} columns")
    return clean_data

# Get lower and upper bounds for IQR method
def get_iqr_bounds(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    return lower_bound, upper_bound

# Remove outliers for specified columns using IQR method
def remove_iqr_outliers(data, columns):
    initial_rows_count = data.shape[0]
    clean_data = data

    for col in columns:
        lower_bound, upper_bound = get_iqr_bounds(data, col)
        clean_data = clean_data[(clean_data[col] >= lower_bound) & 
                                (clean_data[col] <= upper_bound)]
    
    logging.info(f"Outlier removal done. Removed {initial_rows_count - clean_data.shape[0]} rows.")
    
    return clean_data