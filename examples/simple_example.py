# MIT License
#
# Copyright (c) 2018 Tom Runia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to conditions.
#
# Author: Tom Runia
# Date Created: 2018-04-16

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from wavelets_pytorch.transform import WaveletTransform        # SciPy version
from wavelets_pytorch.transform import WaveletTransformTorch   # PyTorch version

dt = 0.1         # sampling frequency
dj = 0.125       # scale distribution parameter
batch_size = 32  # how many signals to process in parallel

t = np.linspace(0., 10., int(10./dt))

# Sinusoidals with random frequency
frequencies = np.random.uniform(-0.5, 2.0, size=batch_size)
batch = np.asarray([np.sin(2*np.pi*f*t) for f in frequencies])

# Initialize wavelet filter banks (scipy and torch implementation)
wa_scipy = WaveletTransform(dt, dj)
wa_torch = WaveletTransformTorch(dt, dj, cuda=True)

# Performing wavelet transform (and compute scalogram)
cwt_scipy = wa_scipy.cwt(batch)
cwt_torch = wa_torch.cwt(batch)

# For plotting, see the examples/plot.py function.
# ...