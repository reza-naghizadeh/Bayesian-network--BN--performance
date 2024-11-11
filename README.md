## Overview

This Python script processes time-series data and Bayesian Network (BN) files, evaluates the configurations of the networks, and computes scores to determine which BN model performs better. It uses a scoring function based on the occurrences of unique configurations within the dataset to compare the two BNs, and the results are outputted along with the final decision on the better-performing BN.

This code was developed as part of my Probabilistic Graphical Models (PGM) course project at IASBS.

## Requirements

To run the script, you need the following dependencies:

- **Python 3.x**
- **NumPy** (for handling array manipulations)

You can install NumPy using pip if it is not already installed:

```bash
pip install numpy
```

## Files

1. `insilico_size10_1_timeseries.txt`: This file contains the time-series dataset (with one column as the time index and others as gene expression values).
2. `net1.txt`: This file contains the first Bayesian Network model.
3. `net2.txt`: This file contains the second Bayesian Network model.

## Script Explanation

### Functions

- **readData()**: Reads and processes the three input files (`insilico_size10_1_timeseries.txt`, `net1.txt`, `net2.txt`), removes unnecessary columns, and converts the data to `float` for calculation.
  
- **preProcess(df1)**: Processes the dataset (`df1`) by comparing each value with the average of the dataset and converting values greater than or equal to the average to 1 and others to 0.

- **configurations(df1, df)**: Identifies the unique configurations of the dataset based on a Bayesian Network, calculates the score for each configuration, and sums them up.

- **score(df1, dd, d, k)**: Computes the score for a given configuration by calculating the log-probabilities of `1`s and `0`s in the configurations.

- **betterOne(finalScoreForDf2, finalScoreForDf3)**: Compares the final scores of two Bayesian Networks and returns the one with the lower score.

- **printOut(df1, df2, df3, finalScoreForDf2, finalScoreForDf3, finalResult)**: Prints the dataset, both Bayesian Networks, their final scores, and the results of the comparison.

### Main Process

The `main()` function performs the following steps:

1. Reads the input data using `readData()`.
2. Processes the dataset using `preProcess()`.
3. Computes the configurations and scores for both Bayesian Networks using `configurations()` and `score()`.
4. Compares the scores of the two Bayesian Networks using `betterOne()` to determine the better network.
5. Outputs the dataset, the Bayesian Networks, their scores, and the final result using `printOut()`.

## Usage

1. Ensure the required input files (`insilico_size10_1_timeseries.txt`, `net1.txt`, `net2.txt`) are in the same directory as the script.
2. Run the script by executing:

```bash
python script_name.py
```

3. The script will print the dataset, both Bayesian Networks, their final scores, and the comparison results, indicating which Bayesian Network model performed better.
