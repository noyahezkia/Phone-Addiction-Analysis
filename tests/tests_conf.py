import pytest
import pandas as pd
import numpy as np

# Create sample data for the testing 
@pytest.fixture
def sample_data():
    np.random.seed(42)
    data = {
        "Addiction_Level": np.random.randint(1, 11, 100),
        "Time_on_Education": np.random.uniform(0, 5, 100),
        "Time_on_Social_Media": np.random.uniform(0, 8, 100),
        "Time_on_Gaming": np.random.uniform(0, 4, 100),
        "Daily_Usage_Hours": np.random.uniform(2, 12, 100),
        "Phone_Usage_Purpose": np.random.choice(["Education", "Social", "Gaming"], 100),
        "Age": np.random.randint(13, 19, 100)
    }
    return pd.DataFrame(data)