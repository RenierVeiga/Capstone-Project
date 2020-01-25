import numpy as np
import pandas as pd


def add_noise(in_data):
    data = pd.DataFrame(in_data)
    mean, std = 1, 0.001
    noise = np.random.normal(mean, std, data.shape)
    return data * noise
