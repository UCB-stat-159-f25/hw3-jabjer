import numpy as np
from ligotools.utils import whiten, reqshift

# check that whiten returns an array of the same shape as the input
def test_whiten_shape():
    shape = whiten(np.zeros(8), lambda f: np.ones_like(f), 0.25).shape
    assert shape == (8,)

# check that reqshift preserves the input length
def test_reqshift_len():
    length = len(reqshift(np.zeros(16), fshift=100, sample_rate=400))
    assert length == 16