import logging
from scipy.stats import ttest_ind, f_oneway

# Perform independent t-test between two numeric samples, two data lists. 
def ttest_two_samples(first_sample, second_sample, label_a, label_b):
    t_stat, p_val = ttest_ind(first_sample, second_sample, equal_var=False)

    logging.info(
        f"T-test | {label_a} vs {label_b} | "
        f"first_mean={first_sample.mean():.2f}, "
        f"second_mean={second_sample.mean():.2f}, "
        f"t={t_stat:.3f}, p={p_val:.4f}"
    )

    return {
        "first_mean": first_sample.mean(),
        "second_mean": second_sample.mean(),
        "t": t_stat,
        "p": p_val
    }

# Perform one way ANOVA between categorial variable the numeric variable
def one_way_anova(data, categorial_col, target_col):
    
    # Split to groups according to the categorical variable values
    groups = [
        data[data[categorial_col] == value][target_col]
        for value in data[categorial_col].unique()
    ]

    # Perform the one way ANOVA
    f_stat, p_val = f_oneway(*groups)

    logging.info(
        f"One-way ANOVA on {categorial_col}: "
        f"F={f_stat:.3f}, p={p_val:.4f}"
    )

    return f_stat, p_val
