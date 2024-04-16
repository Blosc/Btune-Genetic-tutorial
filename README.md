# Btune-Genetic-tutorial

Btune is a dynamic plugin for Blosc2 that can help you find the optimal combination of compression parameters for your datasets. Depending on your needs, Btune has three different tiers of support for tuning datasets:

+ **Genetic**: Btune can be used to find the best compression parameters for a given dataset.  This is done by using a genetic algorithm that tries to find the best combination of parameters for a given dataset.  This is the default mode of operation and is totally free (as in beer and as in freedom).

+ **Trained (Btune Models)**: The goal is automatically selecting the best compression parameters, but using a previously trained model.  This is done by using a neural network that has been trained with a large number of data chunks.  This mode is much faster to operate than the genetic mode, but it requires a donation to the Blosc project.

+ **Fully managed (Btune Studio)**: The user receives a license to use our training software, which enables on-site training for an unlimited number of datasets.  This is done by using a neural network that has been trained with a large number of data chunks.  It requires a donation to the Blosc project.

In this tutorial, we will see how to use the genetic mode of Btune, with a small incursion to the Btune models.  For more information about Btune, check out: https://btune.blosc.org

## Preliminaries

First, clone this repo with:

    git clone https://github.com/Blosc/Btune-Genetic-tutorial

Then, make sure that you are using a Python environment with Python 3.10 or 3.11.  For example, if you are using conda, you can do that easily with:

    conda create -n btune-tutorial python=3.11
    conda activate btune-tutorial

Install the Btune plugin:

    pip install blosc2-btune -U

## Genetic tuning

To use Btune with Blosc2, set the `BTUNE_TRADEOFF` environment variable to a floating-point number between 0 (to optimize speed) and 1 (to optimize compression ratio). Additionally, you can use `BTUNE_PERF_MODE` to optimize compression, decompression, or to achieve a balance between the two by setting it to `COMP`, `DECOMP`, or `BALANCED`, respectively.

**Note**: Most of the environment variables in this tutorial can be set in the `btune_params` dict in the `compr_bench.py` script. If you prefer to set them in the script, just uncomment the lines around line 21.  However, you need to set at least the `BTUNE_TRADEOFF` and `BTUNE_TRACE` environment variables in the shell for Btune operation.

For a trace of what is going on, set the `BTUNE_TRACE` environment variable.  With that, go to a (bash) shell and type:

```bash
BTUNE_TRACE=1 BTUNE_TRADEOFF=0.5 BTUNE_PERF_MODE=COMP python compr_bench.py
```

```
Creating data for genetic exploration purposes...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.1.2
Performance Mode: COMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 10, Repeat Mode - STOP
TRACE: Environment variable BTUNE_MODELS_DIR is not defined
WARNING: Empty metadata, no inference performed
|    Codec   | Filter | Split | C.Level | C.Threads | D.Threads |  S.Score  |  C.Ratio   |   Btune State   | Readapt | Winner
|        lz4 |      0 |     1 |       8 |        16 |        16 |      7.75 |      2.07x |    CODEC_FILTER |    HARD | W
|        lz4 |      0 |     0 |       8 |        16 |        16 |       6.5 |      2.08x |    CODEC_FILTER |    HARD | -
|        lz4 |      1 |     1 |       8 |        16 |        16 |      25.8 |         4x |    CODEC_FILTER |    HARD | W
|        lz4 |      1 |     0 |       8 |        16 |        16 |        25 |      3.93x |    CODEC_FILTER |    HARD | -
|        lz4 |      2 |     1 |       8 |        16 |        16 |        17 |      4.56x |    CODEC_FILTER |    HARD | -
|        lz4 |      2 |     0 |       8 |        16 |        16 |      20.3 |      4.49x |    CODEC_FILTER |    HARD | -
|    blosclz |      0 |     1 |       8 |        16 |        16 |      4.64 |      2.08x |    CODEC_FILTER |    HARD | -
|    blosclz |      0 |     0 |       8 |        16 |        16 |      5.09 |       2.1x |    CODEC_FILTER |    HARD | -
|    blosclz |      1 |     1 |       8 |        16 |        16 |      21.5 |         4x |    CODEC_FILTER |    HARD | -
|    blosclz |      1 |     0 |       8 |        16 |        16 |      7.04 |         1x |    CODEC_FILTER |    HARD | -
|    blosclz |      2 |     1 |       8 |        16 |        16 |      16.6 |         4x |    CODEC_FILTER |    HARD | -
|    blosclz |      2 |     0 |       8 |        16 |        16 |      6.73 |         1x |    CODEC_FILTER |    HARD | -
|        lz4 |      1 |     1 |       8 |        18 |        16 |      14.8 |         4x |    THREADS_COMP |    HARD | -
|        lz4 |      1 |     1 |       8 |        14 |        16 |      15.7 |         4x |    THREADS_COMP |    HARD | -
|        lz4 |      1 |     1 |       7 |        16 |        16 |      17.2 |         4x |          CLEVEL |    HARD | -
|        lz4 |      1 |     1 |       9 |        16 |        16 |      26.6 |         4x |          CLEVEL |    HARD | W
|        lz4 |      1 |     1 |       8 |        16 |        16 |      24.2 |         4x |          CLEVEL |    SOFT | -
<snip>
NDArray created! 3.28x, cspeed=5.95 GB/s
 size=3.00 GB, csize=0.91 GB
 time=0.50 s
type    : NDArray
shape   : (400000000,)
chunks  : (4194304,)
blocks  : (32768,)
dtype   : int64
cratio  : 3.28
cparams : {'blocksize': 262144,
 'clevel': 1,
 'codec': <Codec.ZSTD: 5>,
 'codec_meta': 0,
 'filters': [<Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>,
             <Filter.SHUFFLE: 1>],
 'filters_meta': [0, 0, 0, 0, 0, 0],
 'nthreads': 16,
 'splitmode': <SplitMode.ALWAYS_SPLIT: 1>,
 'typesize': 8,
 'use_dict': 0}
dparams : {'nthreads': 16}

NDarray decompressed in one go: 0.47 s, dspeed=6.41 GB/s
Sum NumPy in 0.12 s, speed=24.43 GB/s
Decompress chunk by chunk: 0.07 s, dspeed=42.88 GB/s
Decompress and sum chunk by chunk: 0.15 s, dspeed=20.43 GB/s
Decompression and checksum OK!
```

Cool! We have done our first attempt at guessing the best parameters.  Read below for a small explanation of the output.

In the `Filter` column you can see the Blosc2 filter that has been selected. 0 means no filter has been used, 1 means `Shuffle` filter and 2 means `BitShuffle` filter. The `Split` column means whether the codec goes over the whole block (0) or if it splits the blocks in parts (of size blocksize/typesize) and compresses them separately (1). Finally, the column `S.Score` displays an estimation of the speed of compression/decompression/transmission_time, dependending of the performance mode. The other columns should be self-explanatory.

You can see in the column `Winner` whether the combination is a winner (`W`), it does not improve the previous winner (`-`) or it is a special value chunk (`S`) meaning that it is trivially compressible, no matter the compression parameters; in the latter case Btune cannot determine whether this is a winner or not.

Note that the tweaking of parameters is done in a 'gentle' mode, i.e. the parameters are changed one by one for every step.  This is done to avoid too much oscillation in the genetic algorithm who decides the winner combination.

### Exercise 1: experiment with different parameters in COMP performance mode

Execute the previous command changing the different parameters (passed as environment variables).  Some examples:

- BTUNE_TRADEOFF=0.1 BTUNE_PERF_MODE=COMP
- BTUNE_TRADEOFF=0.9 BTUNE_PERF_MODE=COMP
- BTUNE_TRADEOFF=1.0 BTUNE_PERF_MODE=COMP
- BTUNE_TRADEOFF=.0 BTUNE_PERF_MODE=COMP

Look at the score and the compression ratios columns.  The smaller the score, the less time it takes to compress/decompress (the faster it is).  Compression ratios are expressed as [uncompressed size / compressed size](https://en.wikipedia.org/wiki/Data_compression_ratio), i.e. the larger, the more storage is saved.

### Questions

+ Which are the codecs and filters that win for tradeoffs favoring compression speed?  Which are the winners for compression ratio?
+ Which are the filters that win for tradeoffs favoring compression speed?  Which are the winners for compression ratio?
+ What happens at extreme values of `BTUNE_TRADEOFF` (0 and 1)?
+ With the best guesses, what is the compression ratio and the compression speed achieved by the bench without Btune?

**Hint**: activate the changes in the `compr_bench.py` (around line 21) and run it again without Btune.  You should see something like:

```bash

```bash
$ python compr_bench.py
Creating data for genetic exploration purposes...
NDArray created! 4.02x, cspeed=8.32 GB/s
 size=3.00 GB, csize=0.75 GB
 time=0.36 s
type    : NDArray
shape   : (400000000,)
chunks  : (4194304,)
blocks  : (32768,)
dtype   : int64
cratio  : 4.02
cparams : {'blocksize': 262144,
 'clevel': 3,
 'codec': <Codec.LZ4: 1>,
 'codec_meta': 0,
 'filters': [<Filter.SHUFFLE: 1>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>],
 'filters_meta': [0, 0, 0, 0, 0, 0],
 'nthreads': 16,
 'splitmode': <SplitMode.ALWAYS_SPLIT: 1>,
 'typesize': 8,
 'use_dict': 0}
dparams : {'nthreads': 16}

NDarray decompressed in one go: 0.46 s, dspeed=6.52 GB/s
Sum NumPy in 0.12 s, speed=26.00 GB/s
Decompress chunk by chunk: 0.05 s, dspeed=64.24 GB/s
Decompress and sum chunk by chunk: 0.12 s, dspeed=24.71 GB/s
Decompression and checksum OK!
```

### Exercise 2: experiment with different parameters in DECOMP performance mode

The DECOMP performance mode only takes decompression time for computing the score.  Execute the previous command changing the different parameters (passed as environment variables).  Some examples:

- BTUNE_TRADEOFF=0.5 BTUNE_PERF_MODE=DECOMP
- BTUNE_TRADEOFF=0.1 BTUNE_PERF_MODE=DECOMP
- BTUNE_TRADEOFF=0.9 BTUNE_PERF_MODE=DECOMP
- BTUNE_TRADEOFF=1.0 BTUNE_PERF_MODE=DECOMP
- BTUNE_TRADEOFF=.0 BTUNE_PERF_MODE=DECOMP

### Questions

+ Which are the codecs and filters that win for tradeoffs favoring decompression speed?  Which are the winners for compression ratio?
+ What's the perceived difference when `BTUNE_PERF_MODE` is set to 'COMP' and 'DECOMP' respectively?
+ What happens at extreme values of `BTUNE_TRADEOFF` (0 and 1)?
+ With the best guesses, what is the compression ratio and the decompression speed achieved by the bench without Btune?

### Exercise 3: experiment with different parameters in BALANCED performance mode

The BALANCED performance mode is a compromise between the previous two modes.  Execute the previous command changing the different parameters (passed as environment variables).  Some examples:

- BTUNE_TRADEOFF=0.5 BTUNE_PERF_MODE=BALANCED
- BTUNE_TRADEOFF=0.1 BTUNE_PERF_MODE=BALANCED
- BTUNE_TRADEOFF=0.9 BTUNE_PERF_MODE=BALANCED
- BTUNE_TRADEOFF=1.0 BTUNE_PERF_MODE=BALANCED
- BTUNE_TRADEOFF=.0 BTUNE_PERF_MODE=BALANCED

### Questions

+ Which are the codecs and filters that win for tradeoffs favoring a balanced speed?  Which are the winners for compression ratio?
+ What's the perceived difference when `BTUNE_PERF_MODE` is set to 'COMP' and 'DECOMP' respectively?
+ What happens at extreme values of `BTUNE_TRADEOFF` (0 and 1)?
+ With the best guesses, what is the compression ratio and the compression/decompression speed achieved by the bench without Btune?

## Using trained Btune models

Btune can use previously trained models to speed up the process of finding the best parameters without manual intervention.  They are in the models directory.  Let's see how to use them.

### Inference (predictions) in COMPression mode

Let's do the inference for COMPression performance mode:

```shell
 BTUNE_TRADEOFF=0.5 BTUNE_USE_INFERENCE=-1 BTUNE_PERF_MODE=COMP BTUNE_TRACE=1  BTUNE_MODELS_DIR=models python compr_bench.py
```

and the output is something like:

```
Creating data for genetic exploration purposes...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.1.2
Performance Mode: COMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 10, Repeat Mode - STOP
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
TRACE: time load model: 0.000873
TRACE: Inference category=33 codec=0 filter=1 clevel=5 splitmode=1 time entropy=0.002269 inference=0.000019
|    Codec   | Filter | Split | C.Level | C.Threads | D.Threads |  S.Score  |  C.Ratio   |   Btune State   | Readapt | Winner
|    blosclz |      1 |     1 |       5 |        16 |        16 |      18.3 |         4x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=33 codec=0 filter=1 clevel=5 splitmode=1 time entropy=0.000451 inference=0.000010
|    blosclz |      1 |     1 |       5 |        16 |        16 |      21.1 |         4x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=33 codec=0 filter=1 clevel=5 splitmode=1 time entropy=0.000680 inference=0.000010
|    blosclz |      1 |     1 |       5 |        16 |        16 |      20.1 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=33 codec=0 filter=1 clevel=5 splitmode=1 time entropy=0.000515 inference=0.000010
|    blosclz |      1 |     1 |       5 |        16 |        16 |      23.5 |         4x |    CODEC_FILTER |    HARD | W
<snip>
NDArray created! 4.03x, cspeed=7.26 GB/s
 size=3.00 GB, csize=0.75 GB
 time=0.41 s
type    : NDArray
shape   : (400000000,)
chunks  : (4194304,)
blocks  : (32768,)
dtype   : int64
cratio  : 4.03
cparams : {'blocksize': 262144,
 'clevel': 3,
 'codec': <Codec.LZ4: 1>,
 'codec_meta': 0,
 'filters': [<Filter.SHUFFLE: 1>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>,
             <Filter.NOFILTER: 0>],
 'filters_meta': [0, 0, 0, 0, 0, 0],
 'nthreads': 16,
 'splitmode': <SplitMode.ALWAYS_SPLIT: 1>,
 'typesize': 8,
 'use_dict': 0}
dparams : {'nthreads': 16}

NDarray decompressed in one go: 0.44 s, dspeed=6.83 GB/s
Sum NumPy in 0.12 s, speed=25.81 GB/s
Decompress chunk by chunk: 0.05 s, dspeed=63.46 GB/s
Decompress and sum chunk by chunk: 0.12 s, dspeed=24.17 GB/s
Decompression and checksum OK!
```

We see how the inference is done for all the chunks (`BTUNE_USE_INFERENCE=-1`) and then the best parameters are used for the rest of the chunks.

## Final words

We have seen how Btune helps you in finding the best compression parameters for specific datasets.  In the previous exercises, we have used a synthetic dataset, but you can use your own data and let Btune help you in finding the best parameters for it.  An easy way to test with your data, is to create a NumPy array out of it, and export it to the Blosc2 format via the [blosc2.asarray() function](https://www.blosc.org/python-blosc2/reference/autofiles/ndarray/blosc2.asarray.html).  Then, you can use the `compr_bench.py` script to test the different parameters.

That's all folks; hope you have enjoyed the ride!  For more information about Btune, check out: https://ironarray.io/btune

Inquiries?  contact@ironarray.io
