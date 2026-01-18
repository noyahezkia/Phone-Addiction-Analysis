from src.correlations import get_pearson_correlations, linear_regression
from src.group_comparisons import ttest_two_samples, one_way_anova

# Test correlation function for returning a dictionary and r value in range
def test_get_pearson_correlations(sample_data):
    features = ['Time_on_Education', 'Time_on_Social_Media']
    results = get_pearson_correlations(sample_data, 'Addiction_Level', features)
    assert 'Time_on_Education' in results
    assert -1 <= results['Time_on_Education'] <= 1

# Test ttest_two_samples for returning p and t values properly
def test_ttest_two_samples(sample_data):
    group_a = sample_data[sample_data['Phone_Usage_Purpose'] == 'Education']['Addiction_Level']
    group_b = sample_data[sample_data['Phone_Usage_Purpose'] == 'Social']['Addiction_Level']
    results = ttest_two_samples(group_a, group_b)
    assert 'p' in results
    assert 't' in results
    assert 0 <= results['p'] <= 1

# Test ANOVA for returning f and p values properly
def test_one_way_anova(sample_data):
    f_stat, p_val = one_way_anova(sample_data, 'Phone_Usage_Purpose', 'Addiction_Level')
    assert f_stat >= 0, f"F-statistic should be non-negative, got {f_stat}"
    assert 0 <= p_val <= 1, f"p-value should be between 0 and 1, got {p_val}"

# Test linear_regression for model returning the correct coefficient amount
def test_linear_regression(sample_data):
    features = ['Time_on_Education', 'Age']
    model = linear_regression(sample_data, 'Addiction_Level', features)
    assert hasattr(model, 'rsquared')
    assert len(model.params) == 3 