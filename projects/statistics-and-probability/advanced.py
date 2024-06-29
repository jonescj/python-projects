import numpy as np
import scipy.stats as stats
from typing import List, Tuple

def anova(*groups: List[float]) -> Tuple[float, float]:
    """
    Perform ANOVA (Analysis of Variance)
    
    :param groups: Variable number of lists containing numerical data for each group.
    :return: F-value and p-value
    """
    f_val, p_val = stats.f_oneway(*groups)
    return f_val, p_val

def one_way_anova(group1: List[float], group2: List[float], group3: List[float]) -> Tuple[float, float]:
    """
    Perform One-Way ANOVA (Analysis of Variance)
    
    :param group1: List of numerical data for group 1
    :param group2: List of numerical data for group 2
    :param group3: List of numerical data for group 3
    :return: F-value and p-value
    """
    f_val, p_val = stats.f_oneway(group1, group2, group3)
    return f_val, p_val

def chi_square_test(observed: List[int], expected: List[int]) -> Tuple[float, float]:
    """
    Perform Chi-Square Test
    
    :param observed: List of observed frequencies
    :param expected: List of expected frequencies
    :return: Chi-square value and p-value
    """
    chi2, p_val = stats.chisquare(f_obs=observed, f_exp=expected)
    return chi2, p_val

def chi_square_test_independence(observed: np.ndarray) -> Tuple[float, float, int, np.ndarray]:
    """
    Perform Chi-Square Test for Independence
    
    :param observed: 2D array of observed frequencies
    :return: Chi-square value, p-value, degrees of freedom, and expected frequencies
    """
    chi2, p_val, dof, expected = stats.chi2_contingency(observed)
    return chi2, p_val, dof, expected

def wilcoxon_rank_sum_test(group1: List[float], group2: List[float]) -> Tuple[float, float]:
    """
    Perform Wilcoxon Rank-Sum Test
    
    :param group1: List of numerical data for group 1
    :param group2: List of numerical data for group 2
    :return: Test statistic and p-value
    """
    stat, p_val = stats.ranksums(group1, group2)
    return stat, p_val

def kruskal_wallis_test(*groups: List[float]) -> Tuple[float, float]:
    """
    Perform Kruskal-Wallis Test
    
    :param groups: Variable number of lists containing numerical data for each group.
    :return: Test statistic and p-value
    """
    stat, p_val = stats.kruskal(*groups)
    return stat, p_val

def friedman_test(*groups: List[float]) -> Tuple[float, float]:
    """
    Perform Friedman Test
    
    :param groups: Variable number of lists containing numerical data for each group.
    :return: Test statistic and p-value
    """
    stat, p_val = stats.friedmanchisquare(*groups)
    return stat, p_val

# Example usage
if __name__ == "__main__":
    group1 = [1, 2, 3, 4, 5]
    group2 = [2, 3, 4, 5, 6]
    group3 = [3, 4, 5, 6, 7]
    
    # ANOVA
    print("ANOVA:", anova(group1, group2, group3))
    
    # One-Way ANOVA
    print("One-Way ANOVA:", one_way_anova(group1, group2, group3))
    
    # Chi-Square Test
    observed = [10, 20, 30]
    expected = [15, 15, 30]
    print("Chi-Square Test:", chi_square_test(observed, expected))
    
    # Chi-Square Test for Independence
    observed = np.array([[10, 10, 20], [20, 20, 20]])
    print("Chi-Square Test for Independence:", chi_square_test_independence(observed))
    
    # Wilcoxon Rank-Sum Test
    print("Wilcoxon Rank-Sum Test:", wilcoxon_rank_sum_test(group1, group2))
    
    # Kruskal-Wallis Test
    print("Kruskal-Wallis Test:", kruskal_wallis_test(group1, group2, group3))
    
    # Friedman Test
    print("Friedman Test:", friedman_test(group1, group2, group3))

from sklearn.decomposition import PCA

def perform_pca(X, n_components=2):
    """
    Perform Principal Component Analysis (PCA).
    
    Parameters:
    X (DataFrame or array-like): Features
    n_components (int): Number of principal components to compute
    
    Returns:
    dict: Dictionary containing PCA model and transformed data
    """
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)
    
    return {
        'pca_model': pca,
        'transformed_data': X_pca
    }
import statsmodels.api as sm
import pandas as pd

def time_series_analysis(data, column, order=(1, 1, 1)):
    """
    Perform Time Series Analysis using ARIMA model.
    
    Parameters:
    data (DataFrame): DataFrame containing the time series data
    column (str): Column name of the time series data
    order (tuple): The (p,d,q) order of the model for the number of AR parameters, differences, and MA parameters
    
    Returns:
    dict: Dictionary containing ARIMA model and fitted values
    """
    model = sm.tsa.ARIMA(data[column], order=order)
    results = model.fit()
    
    return {
        'model': results,
        'fitted_values': results.fittedvalues
    }

from lifelines import KaplanMeierFitter

def survival_analysis(durations, event_observed):
    """
    Perform Survival Analysis using Kaplan-Meier estimator.
    
    Parameters:
    durations (array-like): Durations for the event/censoring
    event_observed (array-like): Boolean array indicating if the event was observed
    
    Returns:
    KaplanMeierFitter: Fitted Kaplan-Meier estimator
    """
    kmf = KaplanMeierFitter()
    kmf.fit(durations, event_observed)
    
    return kmf
