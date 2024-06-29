import math
from scipy.stats import binom, poisson, norm

def probability_event(successes, trials):
    """Determine the Probability of an Event E."""
    return successes / trials

def addition_rule_of_probability(p_a, p_b, p_a_and_b):
    """Displays the Addition Rule of Probability."""
    return p_a + p_b - p_a_and_b

def multiplication_rule_of_probability(p_a, p_b_given_a):
    """Displays the Multiplication Rule of Probability."""
    return p_a * p_b_given_a

def binomial_distribution(n, p, k):
    """Determines the Binomial Distribution."""
    return binom.pmf(k, n, p)

def poisson_distribution(lmbda, k):
    """Determines the Poisson Distribution."""
    return poisson.pmf(k, lmbda)

def gaussian_distribution(mu, sigma, x):
    """Determines the Gaussian distribution."""
    return norm.pdf(x, mu, sigma)

def expected_value_discrete(probabilities, values):
    """Determines the expected value (mean) for a discrete set of random variables."""
    return sum(p * v for p, v in zip(probabilities, values))

def expected_value_continuous(f, a, b, n=1000):
    """Determines the expected value (mean) for a continuous set of random variables."""
    step = (b - a) / n
    total = 0
    for i in range(n):
        total += f(a + i * step) * step
    return total

def standard_deviation(variance):
    """Determines the standard deviation given the variance."""
    return math.sqrt(variance)

# Example usage:
# Probability of an event
print(probability_event(30, 100))  # Example: 30 successes in 100 trials

# Addition rule
print(addition_rule_of_probability(0.5, 0.3, 0.1))  # P(A) = 0.5, P(B) = 0.3, P(A and B) = 0.1

# Multiplication rule
print(multiplication_rule_of_probability(0.5, 0.2))  # P(A) = 0.5, P(B|A) = 0.2

# Binomial distribution
print(binomial_distribution(10, 0.5, 3))  # n = 10, p = 0.5, k = 3

# Poisson distribution
print(poisson_distribution(4, 2))  # λ = 4, k = 2

# Gaussian distribution
print(gaussian_distribution(0, 1, 0))  # μ = 0, σ = 1, x = 0

# Expected value (discrete)
print(expected_value_discrete([0.2, 0.3, 0.5], [1, 2, 3]))  # Probabilities and values

# Expected value (continuous)
print(expected_value_continuous(lambda x: x, 0, 1))  # Function f(x) = x over interval [0, 1]

# Standard deviation
print(standard_deviation(4))  # Variance = 4
