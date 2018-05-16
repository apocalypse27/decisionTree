# Decision-Tree-ID3
## Overview
* The code builds decision trees using two heuristics- Impurity Variance and Info-Gain.
* The resulting decision trees and their accuracies can found in the txt files named: - 
* The data sets can be found in the data_sets folders.
* The code also provides to do option post-pruning.

## Running 
Run the following command to get the decision trees and accuracies..<br>
<i>python testDT.py L K "Path to train data" "Path to validation data" "Path to test data" yes/no </i>

* Here L and K are parameters for Pruning.
1. L is the number of iterations we would like to run the Pruning
2. K is the maximum number of non-leaf nodes we would like to prune in each iteration.

* Yes or no indicates whether or not you want to prune your tree.
