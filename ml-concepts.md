# Machine Learning Concepts

*Also see [Software Engineering](https://github.com/johncf/learn-log/blob/master/software-engineering.md)*

Here's a list of ML-related concepts in random order:

- Bias and Variance
  - Bias:
    - a type of error that occurs due to wrong assumptions about data such as assuming data is linear when in reality, data follows a complex function
    - i.e. under-fitting even when there's enough data for proper training
  - Variance:
    - a type of error that gets introduced when the model is too sensitive to variations in training data
    - i.e. over-fitting, resulting in an inability to generalize properly
- Confidence calibration ([TODO](https://wttech.blog/blog/2021/a-guide-to-model-calibration/))
- Cross-validation ([wiki](https://en.wikipedia.org/wiki/Cross-validation_%28statistics%29))
  - Used to estimate how well a model will generalize
  - Perform multiple rounds of training and validation using different partitions of the same set of data
- Data and Concept drift
  - Data drift: Input data seen in production has shifted from data used in training
  - Concept drift: Mapping from input to expected output has changed (compared to training)
    - Will need relabeling of original training data or discarding them and collect new data
- [Feature selection](https://github.com/johncf/learn-log/blob/master/2023-05-01.md#feature-selection)
- [Feature extraction](https://github.com/johncf/learn-log/blob/master/2023-05-01.md#feature-extraction)
- Inductive bias ([wiki](https://en.wikipedia.org/wiki/Inductive_bias))
  - A set of assumptions the model uses to make predictions of unseen inputs (think: inter- and extra-polation)
  - Example: "Occam's razor," assuming that the simplest consistent hypothesis is the best
- [Data Visualization](https://github.com/johncf/learn-log/blob/master/2023-05-01.md#data-visualization)
