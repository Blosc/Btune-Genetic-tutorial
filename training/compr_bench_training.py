#######################################################################
# Copyright (c) 2019-present, Blosc Development Team <blosc@blosc.org>
# All rights reserved.
#
# This source code is licensed under a BSD-style license (found in the
# LICENSE file in the root directory of this source tree)
#######################################################################
import numpy as np
import blosc2
from time import time


# Create the NDArray
rng = np.random.default_rng()
print("Creating data for genetic exploration purposes...")
a = rng.integers(low=0, high=10000, size=int(2e9), dtype=np.int64)

# Compress
cparams = dict()
dparams = dict()
# Specify your own configuration here
#cparams = dict(codec=blosc2.Codec.LZ4, clevel=3, filters=[blosc2.Filter.SHUFFLE], splitmode=blosc2.SplitMode.ALWAYS_SPLIT)
#cparams = dict(codec=blosc2.Codec.ZSTD, clevel=1, filters=[blosc2.Filter.SHUFFLE], splitmode=blosc2.SplitMode.ALWAYS_SPLIT)
chunks, blocks = None, None
chunks, blocks = (4194304 // 4,), (524288 // 4,)
t0 = time()
b = blosc2.asarray(a, cparams=cparams, dparams=dparams,
                   chunks=chunks, blocks=blocks,
                   urlpath="training.b2nd", mode="w")
schunk = b.schunk
t = time() - t0
print(f"NDArray created! {schunk.cratio:.2f}x, cspeed={schunk.nbytes / t / 2**30:.2f} GB/s"
      f"\n size={schunk.nbytes / 2**30:.2f} GB, csize={schunk.cbytes / 2**30:.2f} GB"
      f"\n time={t:.2f} s"
      f"\n{b.info}")
