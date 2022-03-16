import pandas as pd
import numpy as np

def random_dates(start, end, n, unit='D', seed=None):
    if not seed:
      np.random.seed(0)
  
    ndays = (end - start).days + 1
    return pd.to_timedelta(np.random.rand(n) * ndays, unit=unit) + start