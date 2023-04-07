import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 729362937 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    maxi = x.max()
    lmbda = 0.056
    return maxi/2, \
            ((((maxi - lmbda)/(lmbda**(1/len(x)))) + lmbda)/2)
