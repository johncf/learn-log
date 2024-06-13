# ML Design Interview

Tackling the ML design interview, with a focus on **recommender systems**.

## Problem Navigation

Visualize and organize the entire problem and solution space.

- Define the ultimate goal.
  - Example: "improve user engagement", "improve profits without affecting user enjoyment"
- Define proxy events, and business metrics based on them that can measure our progress.
  - Example: "sessions per week", "session length", "click-through rate", "revenue" (for ads), "daily active users" etc.

## Training Data

Identify methods to collect training data. Analyze constraints / risks associated with each proposed method.

- Clarifying questions:
  - What data do we already have?
    - User metadata: demographic data (gender, age-group, location)
    - Ad/post metadata: ad/post contents, tags/topics
    - User engagement data: ad/post clicks/likes, ad/post impressions (with view-time), users own posts, etc.
  - What is the raw data that can be observed?
    - Example: stream of click events, stream of impression events, user-data in a database etc.
    - What kind of data can be collected? What kind of data processing/transformation pipelines do we need to build for it?
    - We could even create a "not relevant" button to gather negative user-feedbacks.
- Possibility of online learning

## Feature Engineering

Identifying the most important features for the specific task. Come up with relevant features (or feature engineering techniques) to train the model.

- Selecting what features to use, and how to represent history of activity
  - Simple examples: time of the day, day of the week, last viewed post(s), days since a post's upload, user/post language, number of previous impressions (without click), user's past history with posts from the same channel, etc.
  - Complex example: average of embeddings of all posts that a user liked/clicked, [bag-of-words](https://en.wikipedia.org/wiki/Bag-of-words_model) representation of topics/tags a user interacted with
- Also read section 4.1 of the paper, Deep Neural Networks for YouTube Recommendations (see References).
- Handling missing feature values (data sparsity and feature coverage)
- Careful about [feature leakage](https://en.wikipedia.org/wiki/Leakage_%28machine_learning%29#Feature_leakage)

## Modeling

Evaluating model choices, and justifying the final decision.
Explain the training process. Anticipate risks and mitigate them.

- Clarifying questions:
  - What is the existing system? (This could be a baseline.)
- Simple baseline model (or performance)
  - A simple recommender system: random recommendations
- Popular techniques:
  - [Collaborative filtering](https://en.wikipedia.org/wiki/Collaborative_filtering) uses other users preferences to build recommendations for a user.
    - User-based filtering (possible example, news feed in Instagram), item-based filtering (possible example, "bought together" in Amazon)
    - Types:
      - Memory-based: similarity search based on user-item interaction matrix
      - Model-based: similarity search based on dimensionality-reduced interaction history
      - Hybrid and more...
    - Similarity between two users could be measured using Pearson correlation (co-variance) or vector cosine (angular) or Jaccard coefficient (binary IoU) on the vector representation of their interaction history
    - Cons: Cannot handle fresh items since there is no interaction history associated with them.
  - [Content-based filtering](https://en.wikipedia.org/wiki/Recommender_system#Content-based_filtering) uses the description/contents of items to provide recommendations based on the user's profile and preferences.
    - Embedding-based approach for items and users, and using a nearest-neighbor search or vector-similarity metrics to predict interest/relevance.
  - Hybrid approaches use collaborative and content-based filtering to improve recommendations.
- Model: What to predict? What are the inputs?
  - Probability of the user liking an ad/post. (A classification problem -- like or not liking.)
  - Relevance of an ad/post to the user. (A regression problem -- user ratings from 1 to 5.)
- Beyond accuracy (post-processing or re-ranking):
  - Intra-list diversity: recommend items from different sources or topics
  - Serendipity: recommend items that are outside the user's engagement history (a pleasant surprise)
  - Novelty: recommend items that are unpopular (an underrated gem)
  - Robustness: recommendation system must be resistant to manipulation (e.g. negative ratings to competitors)
  - Context-awareness: time (morning vs. night, workday vs. holidays), location, type of device, etc.
  - Persistence vs. Temporal diversity: both are important in different scenarios
  - Bias: imbalances in training data can cause biased recommendation
  - Filter bubble: intellectual isolation from opposing views makes the society more polarized
- Model selection, influenced by features, data volume, interpretability requirements, and more.
  - Fewer data -> linear models fare better
  - Normalized (Cross) Entropy to compare models
    - See [Practical Lessons from Predicting Clicks on Ads at Facebook](https://research.facebook.com/publications/practical-lessons-from-predicting-clicks-on-ads-at-facebook/)

## Evaluation & Deployment

Consistent evaluation and deployment techniques.
Justify and articulate the choice of metrics to track.

- Offline evaluation
  - Example: Recall@k, Mean Reciprocal Rank (MRR), Mean Average Precision (mAP), Normalized Discounted Cumulative Gain (nDCG)
  - Progressive evaluation (train on days 1..n; evaluate on days n+1..n+k)
  - With diversity re-rankings, it becomes difficult to evaluate offline
- Online evaluation
  - A/B testing: click-through rate (CTR), session-length over time (weeks), etc.
  - Detecting data drift, and retraining base models
- Debugging a failed model?
- Continuous evaluation and deployment (daily updates?)
- Training data recency and the problem of [Online-Offline Consistency](https://chronon.ai/test_deploy_serve/Online_Offline_Consistency.html)

## References

- Paper: [Deep Neural Networks for YouTube Recommendations](https://dl.acm.org/doi/10.1145/2959100.2959190)
- [Mock Interview: ML design to recommend artists on Spotify](https://www.youtube.com/watch?v=vyZMYlGBSBM)
- [Mock Interview: ML design to predict watch-times on Netflix](https://www.youtube.com/watch?v=BWlmFQ02DIU); the interviewee is a bit passive, which is not ideal, but he has good ideas
- [Evaluating Recommender and Ranking Systems](https://www.evidentlyai.com/ranking-metrics/evaluating-recommender-systems)
- [Article suggested by a Meta recruiter](https://medium.com/@nrkivar/facebook-field-guide-to-ml-3056900e7930), but it's not very helpful.
