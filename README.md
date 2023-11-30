# Btune-Genetic-tutorial

First, clone this repo with:

    git clone https://github.com/Blosc/Btune-Genetic-tutorial

Then, make sure that you are using a Python environment with Python 3.10 or 3.11.  For example, if you are using conda, you can do that easily with:

    conda create -n btune-tutorial python=3.11
    conda activate btune-tutorial

Install the Btune plugin:

    pip install blosc2-btune -U

# Genetic tuning

To use Btune with Blosc2, set the `BTUNE_TRADEOFF` environment variable to a floating-point number between 0 (to optimize speed) and 1 (to optimize compression ratio). Additionally, you can use `BTUNE_PERF_MODE` to optimize compression, decompression, or to achieve a balance between the two by setting it to `COMP`, `DECOMP`, or `BALANCED`, respectively.

For a trace of what is going on, set the `BTUNE_TRACE` environment variable.  With that, go to the `inference/` directory and type:

```
BTUNE_TRACE=1 BTUNE_TRADEOFF=0.5 BTUNE_PERF_MODE=COMP python rand_int.py
```

```
Creating data for genetic/inference purposes...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.1.1.dev
Performance Mode: COMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 10, Repeat Mode - STOP
TRACE: Environment variable BTUNE_MODELS_DIR is not defined
WARNING: Empty metadata, no inference performed
|    Codec   | Filter | Split | C.Level | C.Threads | D.Threads |  S.Score  |  C.Ratio   |   Btune State   | Readapt | Winner
|        lz4 |      0 |     1 |       8 |         6 |         6 |      5.78 |      1.96x |    CODEC_FILTER |    HARD | W
|        lz4 |      0 |     0 |       8 |         6 |         6 |      14.7 |      2.07x |    CODEC_FILTER |    HARD | W
|        lz4 |      1 |     1 |       8 |         6 |         6 |      32.8 |      3.97x |    CODEC_FILTER |    HARD | W
|        lz4 |      1 |     0 |       8 |         6 |         6 |      53.7 |      3.91x |    CODEC_FILTER |    HARD | -
|        lz4 |      2 |     1 |       8 |         6 |         6 |      28.2 |      4.52x |    CODEC_FILTER |    HARD | W
|        lz4 |      2 |     0 |       8 |         6 |         6 |      16.4 |      4.46x |    CODEC_FILTER |    HARD | -
|    blosclz |      0 |     1 |       8 |         6 |         6 |      8.53 |      1.99x |    CODEC_FILTER |    HARD | -
|    blosclz |      0 |     0 |       8 |         6 |         6 |      12.2 |      2.08x |    CODEC_FILTER |    HARD | -
|    blosclz |      1 |     1 |       8 |         6 |         6 |      32.3 |      3.97x |    CODEC_FILTER |    HARD | -
|    blosclz |      1 |     0 |       8 |         6 |         6 |      19.8 |      3.82x |    CODEC_FILTER |    HARD | -
|    blosclz |      2 |     1 |       8 |         6 |         6 |      23.8 |      4.47x |    CODEC_FILTER |    HARD | -
|    blosclz |      2 |     0 |       8 |         6 |         6 |      19.5 |      4.35x |    CODEC_FILTER |    HARD | -
|        lz4 |      2 |     1 |       8 |         6 |         6 |      57.6 |      4.52x |    THREADS_COMP |    HARD | W
|        lz4 |      2 |     1 |       7 |         6 |         6 |      59.3 |      4.52x |          CLEVEL |    HARD | -
|        lz4 |      2 |     1 |       9 |         6 |         6 |      57.4 |      4.52x |          CLEVEL |    HARD | W
|        lz4 |      2 |     1 |       8 |         6 |         6 |      58.8 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       9 |         6 |         6 |      49.2 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       8 |         6 |         6 |        59 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       9 |         6 |         6 |      58.2 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       8 |         6 |         6 |      58.9 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       9 |         6 |         6 |      19.6 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       8 |         6 |         6 |      39.4 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       9 |         6 |         6 |      55.5 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       8 |         6 |         6 |      57.5 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       9 |         6 |         6 |      60.3 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      0 |     1 |       9 |         6 |         6 |      14.7 |      1.97x |    CODEC_FILTER |    HARD | -
|        lz4 |      0 |     0 |       9 |         6 |         6 |      16.2 |      2.07x |    CODEC_FILTER |    HARD | -
|        lz4 |      1 |     1 |       9 |         6 |         6 |      87.6 |      3.97x |    CODEC_FILTER |    HARD | -
|        lz4 |      1 |     0 |       9 |         6 |         6 |      80.6 |      3.91x |    CODEC_FILTER |    HARD | -
|        lz4 |      2 |     1 |       9 |         6 |         6 |      52.4 |      4.52x |    CODEC_FILTER |    HARD | -
NDArray 'rand_int_inference.b2nd' created!
```

Cool! We have done our first attempt at guessing the best parameters.  Read below for a small explanation of the output.

In the `Filter` column you can see the Blosc2 filter that has been selected. 0 means no filter has been used, 1 means `Shuffle` filter and 2 means `BitShuffle` filter. The `Split` column means whether the codec goes over the whole block (0) or if it splits the blocks in parts (of size blocksize/typesize) and compresses them separately (1). Finally, the column `S.Score` displays an estimation of the speed of compression/decompression/transmission_time, dependending of the performance mode. The other columns should be self-explanatory.

You can see in the column `Winner` whether the combination is a winner (`W`), it does not improve the previous winner (`-`) or it is a special value chunk (`S`) meaning that it is trivially compressible, no matter the compression parameters; in the latter case Btune cannot determine whether this is a winner or not.

## Exercise 1: experiment with different parameters in COMP performance mode

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

## Exercise 2: experiment with different parameters in DECOMP performance mode

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

## Exercise 3: experiment with different parameters in BALANCED performance mode

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

# Using trained Btune models [TBD]

With the models, we can predict the best codecs/filters during the creation of new datasets.

## Inference (predictions) in COMPression mode

Let's do the inference for COMPression performance mode:

```shell
cd ../inference
BTUNE_TRADEOFF=0.5 BTUNE_USE_INFERENCE=-1 BTUNE_PERF_MODE=COMP BTUNE_TRACE=1  BTUNE_MODELS_DIR=rand_int_training.model python rand_int.py
```

and the output is something like:

```
Creating data for inference purposes...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: COMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 10, Repeat Mode - STOP
INFO: Model files found in the 'rand_int_training.model' directory
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
TRACE: time load model: 0.013766
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: COMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 11, Repeat Mode - STOP
INFO: Model files found in the 'rand_int_training.model' directory
TRACE: time load model: 0.000186
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000327 inference=0.000830
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |   0.00038 |      3.97x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000142 inference=0.000006
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.36e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000143 inference=0.000005
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |   1.3e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000140 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.33e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000137 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.34e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000204 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  4.58e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000154 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.34e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000111 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.42e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000115 inference=0.000007
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.37e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000109 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.42e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000117 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.47e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000136 inference=0.000007
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  2.48e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000112 inference=0.000008
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.61e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000105 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.43e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000106 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.38e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000102 inference=0.000005
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.35e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000102 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.38e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000104 inference=0.000005
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.39e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000105 inference=0.000005
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.36e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000101 inference=0.000005
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.37e-05 |      3.97x |    CODEC_FILTER |    HARD | -
NDArray 'rand_int_inference.b2nd' created!
```

### Exercise 2: experiment with different parameters in COMP performance mode

In particular, you can try with different tradeoffs:

- BTUNE_TRADEOFF=0.0  # best speed; compression ratio does not matter
- BTUNE_TRADEOFF=0.3  # good speed, but add some weight to cratio
- BTUNE_TRADEOFF=0.5  # a balance between speed and cratio
- BTUNE_TRADEOFF=0.8  # good cratio, but speed is somewhat important too
- BTUNE_TRADEOFF=1.0  # best compression ratio; speed does not matter

Also, you can set `BTUNE_USE_INFERENCE` to a positive value to use inference only for the first iterations; after that, Btune will fall back into a 'gentle' genetic mode, also called 'tweaking', for fine-tuning some params like `clevel` or `splitmode`.  Note that the tweaking will start from the set of compression parameters that have won in the previous

### Exercise3: combine inference and tweaking modes

Try with the next values:

- BTUNE_USE_INFERENCE=3   # only do inference for the first 3 chunks and then use tweaking
- BTUNE_USE_INFERENCE=10  # only do inference for the first 10 chunks and then use tweaking

* How the parameters are tested now?  Can you see the new pattern?
* How predictions differ from complete inference?

## Inference (predictions) in DECOMPression performance mode

Let's use the model in DECOMPression performance mode now:

```shell
BTUNE_TRADEOFF=0.5 BTUNE_USE_INFERENCE=-1 BTUNE_PERF_MODE=DECOMP BTUNE_TRACE=1  BTUNE_MODELS_DIR=rand_int_training.model python rand_int.py
```

```
Creating data for inference purposes...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: DECOMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 10, Repeat Mode - STOP
INFO: Model files found in the 'rand_int_training.model' directory
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
TRACE: time load model: 0.000626
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: DECOMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 11, Repeat Mode - STOP
INFO: Model files found in the 'rand_int_training.model' directory
TRACE: time load model: 0.000159
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000386 inference=0.000073
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000146 |      4.47x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000380 inference=0.000009
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  2.93e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000213 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.27e-05 |      4.47x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000175 inference=0.000026
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.35e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000354 inference=0.000009
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.52e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000110 inference=0.000008
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.43e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=3 codec=0 filter=35 clevel=5 splitmode=2 time entropy=0.000263 inference=0.000007
|    blosclz |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  6.39e-06 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=3 codec=0 filter=35 clevel=5 splitmode=2 time entropy=0.000104 inference=0.000006
|    blosclz |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  6.11e-06 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000131 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.35e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000233 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.29e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000107 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.33e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000104 inference=0.000005
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.25e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000101 inference=0.000005
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.24e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000102 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.27e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000183 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |   1.3e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=3 codec=0 filter=35 clevel=5 splitmode=2 time entropy=0.000105 inference=0.000005
|    blosclz |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  5.83e-06 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000109 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.32e-05 |      4.47x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000106 inference=0.000005
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.27e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000108 inference=0.000005
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.26e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000101 inference=0.000005
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.27e-05 |      4.47x |    CODEC_FILTER |    HARD | -
NDArray 'rand_int_inference.b2nd' created!
```

### Exercise 4: experiment with different parameters in DECOMP performance mode

Go to instructions in exercises 2 and 3 and retry them for DECOMP mode.

## Final exercise: train models with your own datasets!

Go copy the `rand_int.py` script to some other name (e.g. `my_data.py`) and use some other dataset than the one there (you can read them from your favorite format, like HDF5 or Zarr).  Change the name of the output file too (but keep the .b2nd extension, as it will remain a Blosc2 format).  Train with that one, and store the model in another directory.

Indeed, you can bring your own data, create a NumPy array out of it, and export it to the Blosc2 format.  We recommend to make sure to populate the new array with at least 3000 chunks; in our experience, this is a good minimum to ensure a decent training.

Play with the parameters stated in exercises 2 and 3 and get your own conclusions.  Raise your hand and let's have a discussion in case you get 'interesting' results.

That's all folks; hope you have enjoyed the ride!  For more information about Btune, check out: https://btune.blosc.org

Inquiries?  contact@blosc.org
