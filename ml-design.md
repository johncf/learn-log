# ML Design

Tackling the ML design interview, with a focus on **recommender systems**.

## Problem Navigation

Visualize and organize the entire problem and solution space.

- Define the ultimate goal.
  - Example: "improve user engagement", "improve profits without affecting user enjoyment"
- Define proxy events, and business metrics based on them that can measure our progress.
  - Example: "sessions per week", "session length", "click-through rate", "revenue" (for ads), "daily active users" etc.
  - We could even create a "not relevant" button to gather negative user-feedbacks.

## Training Data

Identify methods to collect training data. Analyze constraints / risks associated with each proposed method.

- Clarifying questions:
  - What data do we already have?
    - User metadata: demographic data (gender, age-group, location)
    - Ad/post metadata: ad/post contents, tags/topics
    - User engagement data: user-ad/post clicks, user-ad/post impressions without clicks, users own posts, etc.
  - What is the raw data that can be observed?
    - Example: stream of click events, stream of impression events, user-data in a database etc.
    - What kind of data can be collected? What kind of data processing/transformation pipelines do we need to build for it?
- Training data recency and the problem of [Online-Offline Consistency](https://chronon.ai/test_deploy_serve/Online_Offline_Consistency.html)
- Possibility of online learning
- Minimizing bias in data
- Class imbalances

## Feature Engineering

Identifying the most important features for the specific task. Come up with relevant features (or feature engineering techniques) to train the model.

- Careful about [feature leakage](https://en.wikipedia.org/wiki/Leakage_%28machine_learning%29#Feature_leakage)
- Handling missing feature values (feature coverage)

## Modeling

Evaluating model choices, and justifying the final decision.
Explain the training process. Anticipate risks and mitigate them.

- Clarifying questions:
  - What is the existing system? (This could be a baseline.)
- Simple baseline model (or performance)
  - A simple language model for information extraction: [bag-of-words](https://en.wikipedia.org/wiki/Bag-of-words_model)
- Model selection, influenced by features, data volume, interpretability requirements, and more.
  - Fewer data -> linear models better
  - Normalized (Cross) Entropy to compare models
    - See [Practical Lessons from Predicting Clicks on Ads at Facebook](https://research.facebook.com/publications/practical-lessons-from-predicting-clicks-on-ads-at-facebook/)
- Train metrics: Area Under Curve (AUC), R square, precision, recall

## Evaluation & Deployment

Consistent evaluation and deployment techniques.
Justify and articulate the choice of metrics to track.

- Offline evaluation
  - Progressive evaluation (train on days 1..n; evaluate on days n+1..n+k)
  - Calibration
- Online evaluation
  - Detecting data drift
  - A/B testing and CTR
- Debugging a failed model?
- Continuous evaluation and deployment (daily updates?)

## References

- [Article suggested by a Meta recruiter](https://medium.com/@nrkivar/facebook-field-guide-to-ml-3056900e7930), but it's not very helpful.
