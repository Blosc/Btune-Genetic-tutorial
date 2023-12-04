##############################################################################
# Btune for Blosc2 - Automatically choose the best codec/filter for your data
#
# Copyright (c) 2023 The Blosc Developers <blosc@blosc.org>
# https://btune.blosc.org
# License: GNU Affero General Public License v3.0
# See LICENSE.txt for details about copyright and rights to use.
##############################################################################

import numpy as np

from btune_training import btune_lib as bt
import pandas as pd
import tensorflow as tf
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] not in ["c", "d"]:
        print("Usage example: python training_chunk.py c[cspeed]/d[dspeed] meas_root meas_dir1 meas_dir2...")
        raise Exception("You can only specify whether to use compression speed (c) or decompression speed (d)")

    cspeed = sys.argv[1] == "c"
    meas_root = sys.argv[2]
    meas_dirs = sys.argv[3:]

    probes = [
        'entropy-nofilter-nosplit',
    ]
    categories = [
        'blosclz-nofilter-nosplit-5',
        'blosclz-shuffle-nosplit-5',
        'blosclz-bitshuffle-nosplit-5',
        'blosclz-shuffle-bytedelta-nosplit-5',
        'lz4-nofilter-nosplit-5',
        'lz4-shuffle-nosplit-5',
        'lz4-bitshuffle-nosplit-5',
        'lz4-shuffle-bytedelta-nosplit-5',
        'lz4hc-nofilter-nosplit-5',
        'lz4hc-shuffle-nosplit-5',
        'lz4hc-bitshuffle-nosplit-5',
        'lz4hc-shuffle-bytedelta-nosplit-5',
        'zlib-nofilter-nosplit-5',
        'zlib-shuffle-nosplit-5',
        'zlib-bitshuffle-nosplit-5',
        'zlib-shuffle-bytedelta-nosplit-5',
        'zstd-nofilter-nosplit-1',
        'zstd-shuffle-nosplit-1',
        'zstd-bitshuffle-nosplit-1',
        'zstd-shuffle-bytedelta-nosplit-1',
        'zstd-nofilter-nosplit-3',
        'zstd-shuffle-nosplit-3',
        'zstd-bitshuffle-nosplit-3',
        'zstd-shuffle-bytedelta-nosplit-3',
        'zstd-nofilter-nosplit-6',
        'zstd-shuffle-nosplit-6',
        'zstd-bitshuffle-nosplit-6',
        'zstd-shuffle-bytedelta-nosplit-6',
        'zstd-nofilter-nosplit-9',
        'zstd-shuffle-nosplit-9',
        'zstd-bitshuffle-nosplit-9',
        'zstd-shuffle-bytedelta-nosplit-9',
        'blosclz-nofilter-split-5',
        'blosclz-shuffle-split-5',
        'blosclz-bitshuffle-split-5',
        'blosclz-shuffle-bytedelta-split-5',
        'lz4-nofilter-split-5',
        'lz4-shuffle-split-5',
        'lz4-bitshuffle-split-5',
        'lz4-shuffle-bytedelta-split-5',
        'lz4hc-nofilter-split-5',
        'lz4hc-shuffle-split-5',
        'lz4hc-bitshuffle-split-5',
        'lz4hc-shuffle-bytedelta-split-5',
        'zlib-nofilter-split-5',
        'zlib-shuffle-split-5',
        'zlib-bitshuffle-split-5',
        'zlib-shuffle-bytedelta-split-5',
        'zstd-nofilter-split-1',
        'zstd-shuffle-split-1',
        'zstd-bitshuffle-split-1',
        'zstd-shuffle-bytedelta-split-1',
        'zstd-nofilter-split-3',
        'zstd-shuffle-split-3',
        'zstd-bitshuffle-split-3',
        'zstd-shuffle-bytedelta-split-3',
        'zstd-nofilter-split-6',
        'zstd-shuffle-split-6',
        'zstd-bitshuffle-split-6',
        'zstd-shuffle-bytedelta-split-6',
        'zstd-nofilter-split-9',
        'zstd-shuffle-split-9',
        'zstd-bitshuffle-split-9',
        'zstd-shuffle-bytedelta-split-9',
    ]

    # Load data as dataframes
    probes_dfs, codecs_dfs = bt.load_data_chunk(meas_root=meas_root, meas_dirs=meas_dirs,
                                                probes=probes, categories=categories)
    tradeoffs_array = np.linspace(0, 1, 11, dtype="float32")
    print("Tradeoffs = ", tradeoffs_array)
    # Bests categories for every data sample
    bests = bt.get_labels_tradeoffs(codecs_dfs, tradeoffs_array, cspeed=cspeed)

    # Build input data
    nn_input = bt.get_nn_input(probes_dfs, tradeoffs_array)

    # Split train/test data
    (train_data, train_labels, train_bests), \
        (test_data, test_labels, test_bests) = bt.split_data(nn_input, bests, len(categories))

    # Normalize train test data sets
    suffix = 'comp' if cspeed else 'decomp'
    meta_path = f'model_{suffix}.json'
    train_data, test_data = bt.normalize_train_test(train_data, test_data, meta_path, categories)

    # Train model
    print()
    print('# Model fit')
    model = bt.get_model(len(categories))
    history = model.fit(
        train_data,
        train_labels,
        epochs=20,
        validation_split=0.1,
    )

    # Save model
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    open(f'model_{suffix}.tflite', 'wb').write(tflite_model)

    # Plot
    bt.plot_history(history)

    # Test with train data
    print()
    print('# Prediction with the TRAIN data')
    train_preds = bt.test_prediction(model, train_data, train_bests)

    # Test with test data
    print()
    print('# Prediction with the TEST data')
    test_preds = bt.test_prediction(model, test_data, test_bests)

    # Print most predicted categories for each tradeoff
    print()
    tradeoffs = pd.concat([train_data.tradeoff, test_data.tradeoff], axis=0)
    tradeoffs = tradeoffs.reset_index(drop=True)
    preds = pd.concat([train_preds, test_preds], axis=0).reset_index(drop=True)
    preds = preds.reset_index(drop=True)
    table = bt.most_predicted(preds, tradeoffs, categories, codecs_dfs)
    print(table)

    # Print different scores for each tradeoff
    print()
    bests = pd.concat([train_bests, test_bests], axis=0)
    bests = bests.reset_index(drop=True)
    bt.scores_summary(preds, bests, tradeoffs)

    # Print legend (index to category name)
    print()
    print('# Legend')
    bt.print_legend(probes, categories)
