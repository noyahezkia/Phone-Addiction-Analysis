import logging
import statsmodels.api as sm

# Calculate pearson correlation between one dependent variable and explanatory variables
def get_pearson_correlations(data, target_col, feature_cols):
    results = {}

    # Go over each explanatory variable and save the correlation with the dependent
    for col in feature_cols:
        pearson_corr = data[col].corr(data[target_col])
        results[col] = pearson_corr

        # Log the correlation value 3 digits after floating point
        logging.info(f"Correlation | {col} vs {target_col}: r={pearson_corr:.3f}")

    return results

# Calculate linear resgreesion between one dependent variable and explanatory variables
def linear_regression(data, dependent_col, explanatory_cols):
    
    # Define the explanatory variables dataframe
    explanatory_matrix = data[explanatory_cols]

    # Get the vector of the values we want to predict
    dependent_vector = data[dependent_col]

    # Add y axis interception constant to the explanatory variables matrix
    # The "b" in the linear equation y = ax + b
    explanatory_matrix = sm.add_constant(explanatory_matrix)

    # Define a model predicting the dependent value according to the explanatory values
    model = sm.OLS(dependent_vector, explanatory_matrix).fit()

    logging.info("Regression model fitted")
    logging.info(model.summary().as_text())

    return model
