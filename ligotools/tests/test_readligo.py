import numpy as np
from ligotools import readligo as rl

# check that [0,1,1,0,1] becomes segments [(1,3), (4,5)] when fs=1
def test_dq_channel_to_seglist_basic():
    segs = rl.dq_channel_to_seglist(np.array([0,1,1,0,1]), fs=1)
    assert [(s.start, s.stop) for s in segs] == [(1,3), (4,5)]

# check that [0,1,1,0,1] is converted to GPS segments [(1001,1003), (1004,1005)] when gps_start=1000
def test_dq2segs_from_array():
    segs = rl.dq2segs(np.array([0,1,1,0,1]), gps_start=1000)
    assert list(segs) == [(1001,1003), (1004,1005)]
