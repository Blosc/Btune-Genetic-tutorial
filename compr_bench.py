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
a = rng.integers(low=0, high=10000, size=int(4e8), dtype=np.int64)

# Compress
cparams = dict()
chunks, blocks = None, None
#cparams = dict(codec=blosc2.Codec.LZ4, clevel=9, filters=[blosc2.Filter.SHUFFLE], splitmode=blosc2.SplitMode.ALWAYS_SPLIT)
#cparams = dict(codec=blosc2.Codec.ZSTD, clevel=1, filters=[blosc2.Filter.SHUFFLE], splitmode=blosc2.SplitMode.ALWAYS_SPLIT)
#cparams = dict()
#chunks, blocks = (4194304,), (524288,)
t0 = time()
b = blosc2.asarray(a, cparams=cparams, chunks=chunks, blocks=blocks)
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
print(f"Summed NumPy in {t:.2f} s, speed={b.schunk.nbytes / t / 2**30:.2f} GB/s")

# Decompress chunk by chunk
t0 = time()
for chunk in b.schunk.iterchunks(dtype=b.dtype):
    pass
t = time() - t0
print(f"Decompressed chunk by chunk: {t:.2f} s, dspeed={b.schunk.nbytes / t / 2**30:.2f} GB/s")

# Decompress and sum chunk by chunk
t0 = time()
sum2 = 0
for chunk in b.schunk.iterchunks(dtype=b.dtype):
    sum2 += chunk.sum()
t = time() - t0
print(f"Summed and decompressed chunk by chunk: {t:.2f} s, dspeed={b.schunk.nbytes / t / 2**30:.2f} GB/s")

assert sum1 == sum2
print("Decompression and checksum OK!")
