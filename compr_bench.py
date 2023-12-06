#######################################################################
# Copyright (c) 2019-present, Blosc Development Team <blosc@blosc.org>
# All rights reserved.
#
# This source code is licensed under a BSD-style license (found in the
# LICENSE file in the root directory of this source tree)
#######################################################################
import numpy as np
import blosc2
import blosc2_btune
from time import time
import os


# Create the NDArray
rng = np.random.default_rng()
print("Creating data for genetic exploration purposes...")
a = rng.integers(low=0, high=10000, size=int(4e8), dtype=np.int64)

# Btune environment params
os.environ["BTUNE_TRACE"] = "1"
# Uncomment the following to forcing the use of Btune (or do it in the shell)
#os.environ["BTUNE_TRADEOFF"] = "0.5"  # 0.0 (speed) - 1.0 (compression)
# Btune programmatic params
base_dir = os.path.dirname(__file__)
btune_params = {
    ## genetic exploration
    'perf_mode': blosc2_btune.PerformanceMode.COMP,
    #'cparams_hint': False,   # whether use the cparams specified in the context or not
    #'nwaits': 0,
    #'nsofts': 5,
    #'nhards': 10,
    # behaviour.repeat_mode,
    #'repeat_mode': blosc2_btune.RepeatMode.STOP,
    #'bandwidth': 20 * 1024 ** 2,  # 20 GB/s (expressed in KB/s). Use less for disk-bound cases.
    ## inference (models_dir is required)
    #'models_dir': "%s/models" % base_dir,  # where the models are stored
    #'use_inference': -1,  # number of times inference is applied. If -1, always apply inference
}
blosc2_btune.set_params_defaults(**btune_params)

# Compress params
cparams = dict()
dparams = dict()
# Specify your own configuration here
#cparams = dict(codec=blosc2.Codec.LZ4, clevel=3, filters=[blosc2.Filter.SHUFFLE], splitmode=blosc2.SplitMode.ALWAYS_SPLIT)
#cparams = dict(codec=blosc2.Codec.ZSTD, clevel=1, filters=[blosc2.Filter.SHUFFLE], splitmode=blosc2.SplitMode.ALWAYS_SPLIT)
chunks, blocks = None, None
# Uncomment below to specify your own chunks and blocks (try to match to L3 / L2 cache sizes)
#chunks, blocks = (4194304,), (524288,)
urlpath = None
# Uncomment below to store the data in a file instead of in-memory
#urlpath = "compr_bench.b2nd"

# Compress
t0 = time()
b = blosc2.asarray(a, cparams=cparams, dparams=dparams, chunks=chunks, blocks=blocks, urlpath=urlpath, mode="w")
schunk = b.schunk
t = time() - t0
print(f"NDArray created! {schunk.cratio:.2f}x, cspeed={schunk.nbytes / t / 2**30:.2f} GB/s"
      f"\n size={schunk.nbytes / 2**30:.2f} GB, csize={schunk.cbytes / 2**30:.2f} GB"
      f"\n time={t:.2f} s"
      f"\n{b.info}")

# Decompress
t0 = time()
c = b[:]
t = time() - t0
print(f"NDarray decompressed in one go: {t:.2f} s, dspeed={b.schunk.nbytes / t / 2**30:.2f} GB/s")

# Sum NumPy
t0 = time()
sum1 = c.sum()
t = time() - t0
print(f"Sum NumPy in {t:.2f} s, speed={b.schunk.nbytes / t / 2**30:.2f} GB/s")

# Decompress chunk by chunk
t0 = time()
for chunk in b.schunk.iterchunks(dtype=b.dtype):
    pass
t = time() - t0
print(f"Decompress chunk by chunk: {t:.2f} s, dspeed={b.schunk.nbytes / t / 2**30:.2f} GB/s")

# Decompress and sum chunk by chunk
t0 = time()
sum2 = 0
for chunk in b.schunk.iterchunks(dtype=b.dtype):
    sum2 += chunk.sum()
t = time() - t0
print(f"Decompress and sum chunk by chunk: {t:.2f} s, dspeed={b.schunk.nbytes / t / 2**30:.2f} GB/s")

assert sum1 == sum2
print("Decompression and checksum OK!")
