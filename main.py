from src.logger_config import setup_logger
from consts.paths import DATASET_PATH
from src.data_handler import *
from consts.data_columns import *
from src.correlations import *
from src.group_comparisons import *
from src.visualizations import *

def main():
    setup_logger()

    # Load the dataset from csv file and clean it 
    data = load_csv(DATASET_PATH)
    data = remove_empty_cells(remove_duplicates(data))
    cols_to_clean = [ADDICTION_LEVEL_COL, DAILY_USAGE_COL, EDUCATION_TIME_COL]
    data = remove_iqr_outliers(data, cols_to_clean)

    explanatory_vars = [
        EDUCATION_TIME_COL,
        SOCIAL_MEDIA_TIME_COL,
        GAMING_TIME_COL,
        DAILY_USAGE_COL
    ]

    # Calculate the correlation between the addiction level to its explanatory variables
    correlations = get_pearson_correlations(data, ADDICTION_LEVEL_COL, explanatory_vars)
    bar_plot(correlations, "Correlation with Addiction Level", "Pearson r")

    # Check whether usage content affects addiction level in high usage
    # Calculate general daily usage hours median and get the highest users
    median_total = data[DAILY_USAGE_COL].median()
    top_total_users = data[data[DAILY_USAGE_COL] >= median_total][ADDICTION_LEVEL_COL]

    # Calculate education usage hours median and get the highest users
    median_edu = data[EDUCATION_TIME_COL].median()
    top_education_users = data[data[EDUCATION_TIME_COL] >= 
                               median_edu][ADDICTION_LEVEL_COL]

    ttest_results = ttest_two_samples(
        top_total_users,
        top_education_users,
        "High Total Usage",
        "High Education Usage"
    )

    if ttest_results["p"] < 0.05 and ttest_results["second_mean"] < ttest_results["first_mean"]:
        logging.info(
            "CONCLUSION: Among intensive users, education-oriented usage "
            "is associated with lower addiction levels."
        )

    # Calculate linear regression in order to predict addiction level by the independent
    # variables
    model = linear_regression(data, ADDICTION_LEVEL_COL, explanatory_vars)

    # Perform one way ANOVA 
    f, p = one_way_anova(data, USAGE_PURPOSE_COL, ADDICTION_LEVEL_COL)

    if p < 0.05:
        logging.info("LOGICAL CONCLUSION: Addiction differs by usage purpose.")
    else:
        logging.info("LOGICAL CONCLUSION: Addiction does not differ by usage purpose.")

    box_plot(
        data,
        USAGE_PURPOSE_COL,
        ADDICTION_LEVEL_COL,
        "Addiction Level by Phone Usage Purpose"
    )

    # Extra visualization
    scatter_plot(
        data,
        EDUCATION_TIME_COL,
        ADDICTION_LEVEL_COL,
        "Education Time vs Addiction Level"
    )

if __name__ == "__main__":
    main()
