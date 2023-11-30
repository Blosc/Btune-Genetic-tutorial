#######################################################################
# Copyright (c) 2019-present, Blosc Development Team <blosc@blosc.org>
# All rights reserved.
#
# This source code is licensed under a BSD-style license (found in the
# LICENSE file in the root directory of this source tree)
#######################################################################
import sys
import numpy as np
import blosc2


urlpath = "rand_int_%s.b2nd"
chunks = (5000,)

# Create the NDArray
rng = np.random.default_rng()
if len(sys.argv) > 1 and sys.argv[1] == '-t':
    print("Creating data for training purposes...")
    # Try to train with at least 3k chunks
    a = rng.integers(low=0, high=10000, size=int(2e7), dtype=np.int64)
    urlpath_training = urlpath % "training"
    _ = blosc2.asarray(a, urlpath=urlpath_training, mode="w", chunks=chunks)
    print(f"NDArray '{urlpath_training}' created!")
else:
    print("Creating data for genetic/inference purposes...")
    a = rng.integers(low=0, high=10000, size=int(1e5), dtype=np.int64)
    urlpath_inference = urlpath % "inference"
    _ = blosc2.asarray(a, urlpath=urlpath_inference, mode="w", chunks=chunks)
    print(f"NDArray '{urlpath_inference}' created!")
