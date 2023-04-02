import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 419670097  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    min_x = min(x)
    alpha = 1 - p
    beta = alpha
    left = min((1/2 - expon.ppf(alpha) / (n * min_x)) / 35**2, (1/2 - expon.ppf(1 - beta) / (n * min_x)) / 35**2)
    right = max((1/2 - expon.ppf(alpha) / (n * min_x)) / 35**2, (1/2 - expon.ppf(1 - beta) / (n * min_x)) / 35**2)
    return left, right
