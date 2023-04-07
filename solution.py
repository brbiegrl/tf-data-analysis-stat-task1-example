import pandas as pd
import numpy as np


chat_id = 909631698 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 10; mu = -13; sigma = np.exp(1)
    dist = np.random.norm(mu, sigma, len(x))
    return dist.mean()/t
