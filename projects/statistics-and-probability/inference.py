import scipy.stats as stats
import numpy as np

def hypothesis_testing(sample1, sample2, alpha=0.05):
    """
    Perform hypothesis testing for two samples.
    
    Parameters:
    sample1 (array-like): First sample data.
    sample2 (array-like): Second sample data.
    alpha (float): Significance level, default is 0.05.
    
    Returns:
    tuple: Test statistic, p-value, conclusion
    """
    # Perform a two-sample t-test
    t_stat, p_value = stats.ttest_ind(sample1, sample2)
    
    # Determine whether to reject the null hypothesis
    if p_value < alpha:
        conclusion = "Reject the null hypothesis (H_0)."
    else:
        conclusion = "Fail to reject the null hypothesis (H_0)."
    
    return t_stat, p_value, conclusion

# Example usage
sample1 = np.array([5, 7, 8, 9, 10])
sample2 = np.array([3, 4, 5, 6, 7])
t_stat, p_value, conclusion = hypothesis_testing(sample1, sample2)
print(f"Test Statistic: {t_stat}, P-value: {p_value}, Conclusion: {conclusion}")

import scipy.stats as stats
import numpy as np

def confidence_interval_mean(x, sigma, n, confidence_level=0.95):
    """
    Calculate the confidence interval for the mean.
    
    Parameters:
    x (float): Sample mean.
    sigma (float): Population standard deviation.
    n (int): Sample size.
    confidence_level (float): Confidence level, default is 0.95.
    
    Returns:
    tuple: Lower bound and upper bound of the confidence interval
    """
    z_score = stats.norm.ppf((1 + confidence_level) / 2)
    margin_of_error = z_score * (sigma / np.sqrt(n))
    
    lower_bound = x - margin_of_error
    upper_bound = x + margin_of_error
    
    return lower_bound, upper_bound

# Example usage
x = 50  # Sample mean
sigma = 10  # Population standard deviation
n = 30  # Sample size
confidence_level = 0.95

lower_bound, upper_bound = confidence_interval_mean(x, sigma, n, confidence_level)
print(f"Confidence Interval: ({lower_bound}, {upper_bound})")
