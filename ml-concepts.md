# Machine Learning Concepts

Lists a bunch of concepts in random order.

- Project Lifecycle
  - Scoping: Define the project
    - Define: Realtime or batched, Cloud or edge/browser, Compute resources, Latency, Logging, Privacy
  - Data: Define & establish a baseline, then collect, label and organize
  - Modeling: Select and train, then error analysis
    - How to estimate and tune confidence?
  - Deployment: Deploy, then monitor & maintain
    - Shadow-mode (parallel) deployment, Canary (gradual ramp-up) deployment
    - Monitoring:
      - software metrics (memory, compute, latency etc.)
      - input metrics (input length, fraction of missing values, image brightness)
      - output metrics (fraction of missing values, is null/empty/error)
      - user behavior (rerunning, switching to manual mode etc.)
      - set thresholds for notifications/alarms (for detecting drifts etc.)
- Data/Concept Drift
  - Data Drift: Input data seen in production has shifted from data used in training
  - Concept Drift: Mapping from input to expected output has changed (compared to training)
    - Will need relabeling of original training data or discarding them and collect new data
- Bias and variance
  - Bias:
    - a type of error that occurs due to wrong assumptions about data such as assuming data is linear when in reality, data follows a complex function
    - i.e. under-fitting even when there's enough data for proper training
  - Variance:
    - a type of error that gets introduced when the model is too sensitive to variations in training data
    - i.e. over-fitting, resulting in an inability to generalize properly
- [Cross-validation](https://en.wikipedia.org/wiki/Cross-validation_%28statistics%29)
  - Used to estimate how well a model will generalize
  - Perform multiple rounds of training and validation using different partitions of the same set of data
- [Inductive bias](https://en.wikipedia.org/wiki/Inductive_bias)
  - A set of assumptions the model uses to make predictions of unseen inputs (think: inter- and extra-polation)
  - Example: "Occam's razor," assuming that the simplest consistent hypothesis is the best
