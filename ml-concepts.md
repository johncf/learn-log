# Machine Learning Concepts

Here's a list of ML-related concepts in random order:

## Types of Learning

- [Supervised Learning](https://www.ibm.com/topics/supervised-learning): to approximate a function that maps inputs to outputs based on example input-output pairs.
  - Regression: to predict a continuous output variable (e.g., housing prices)
  - Classification: to predict a categorical output variable (e.g., cat vs. dog images)

- [Unsupervised Learning](https://www.ibm.com/topics/unsupervised-learning): to build a concise representation of, or find patterns in some set of data.
  - Clustering: to group data based on their similarities and differences. (e.g., k-Means clustering, EM clustering)
  - Association Rule Learning: to find interesting relations between features/variables in a dataset, in order to discover the rules that determine how or why certain items are connected. (e.g., Apriori algorithm)
  - Dimensionality Reduction: to compress high-dimensional data into lower dimensions with minimal loss of information. (e.g., PCA, Isomap, Autoencoders)

- [Semi-supervised Learning](https://www.ibm.com/topics/semi-supervised-learning): to train a model using both supervised learning tasks (on labeled datasets) and unsupervised learning tasks (on larger unlabeled datasets), to make the model generalize better than if solely trained without unlabeled data.
  - Relies on certain assumptions about the distribution of unlabeled data such as "cluster assumption", "manifold assumption", "low-density assumption" etc.
  - Two problems to be solved: transductive learning (to label the unlabeled dataset) and inductive learning (to find the generalized function that maps from the input space to the output space).

- [Self-supervised Learning](https://www.ibm.com/topics/self-supervised-learning): to learn useful representations or features from the data that can be fine-tuned for specific downstream tasks.
  - Uses a supervised learning method on unlabeled data by automatically generating supervisory signals based on the structure of the data.
  - This is used in "pretext tasks" to learn meaningful representations of unstructured data.
  - Learned representations are then used in "downstream tasks" with supervised learning or reinforcement learning.
  - Two kinds: Self-predictive learning (e.g. autoencoders) and Contrastive learning (e.g. CLIP).
  - Examples: Transformer-based LLMs like BERT and GPT, image synthesis models like variational autoencoders (VAEs) and GANs to computer vision models like SimCLR and Momentum Contrast (MoCo).

- [Reinforcement Learning](https://www.ibm.com/topics/reinforcement-learning): to train an autonomous agent to make optimal decisions and act in response to its environment, through trial-and-error.
  - Addresses sequential decision-making problems in uncertain and dynamic environments.
  - Literature widely formulate such relationships in terms of Markov decision processes (MDP) or [POMDP](https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process).
  - Basic design: An "Agent" interacts with an "Environment" by taking a series of "Actions", each affecting the "State". The agent receives a "Reward" for each Action, a feedback signal designed to guide the agent towards a desired goal or to enforce certain behavior.
  - An algorithm (e.g. Q-learning) is used to positively reinforce action-sequences that maximize rewards.
  - Exploration-exploitation trade-off: a parameter that controls the ratio of actions that "explores new/unknown states" or "exploits prior knowledge to maximize rewards".
  - Components: Reward signals (pre-defined), Policy (learnt, agent behavior), Value function (optional, learnt, expected future rewards for a state or a state-action pair), and Model (optional, pre-trained, to model the environment).

## Model Selection

- Consider factors: model complexity, interpretability, computational cost, robustness etc.
- Test for low bias: train to over-fit the model on a tiny set of data, to ensure the model is powerful enough.
- Cross-validation ([wiki](https://en.wikipedia.org/wiki/Cross-validation_%28statistics%29))
  - Used to estimate model (or training) robustness, or how well it generalizes
  - Perform multiple rounds of training and validation using different partitions of the same set of data
- Akaike information criterion (AIC, [wiki](https://en.wikipedia.org/wiki/Akaike_information_criterion))
  - A relative score to compare different models on the same dataset.
  - TODO

## Model Training

- Cost function: the function that we optimize during training
  - Cost function = Loss function(s) + Regularization
- Loss function: the penalty for a prediction
  - Regression models: L2 Loss, L1 Loss, Lp Loss, Cosine Similarity, Huber Loss, etc.
  - Classification models: Cross-Entropy Loss, KL Divergence, Hinge Loss, etc.
  - Sequence models: CTC Loss, etc.?
- Regularization: the penalty for model complexity, to keep the model simple.
  - E.g., L1 Regularization (Lasso), L2 Regularization (Ridge), Dropout, etc.
  - See [extra notes](./2023-07.md#regularization).

## Model Evaluation

- Regression models: Mean Squared Error (MSE), Mean Absolute Error (MAE), R-Squared, etc.
- Classification models: Accuracy, Precision, Recall, F1-score, ROC curve and AUC, etc.
- Language models: Perplexity, ROUGE score, BLEU score, etc.
- Clustering models: Internal Evaluation (Silhouette coefficient etc.), External Evaluation (Purity etc.)

## Bias and Variance

- Bias:
  - a type of error that occurs due to wrong assumptions about data such as assuming data is linear when in reality, data follows a complex function
  - i.e. under-fitting even when there's enough data for proper training
- Variance:
  - a type of error that gets introduced when the model is too sensitive to variations in training data
  - i.e. over-fitting, resulting in an inability to generalize properly
- When training a model, the objective/cost function is the sum of *loss function* and *regularization*.
  - The loss function penalizes the model for incorrect predictions (on the training set), thus encouraging reduction in bias.
  - The regularization term is responsible for keeping the model simple, thus encouraging reduction in variance. (Also helps [improve training stability](./2023-07.md#regularization).)
- Inductive bias ([wiki](https://en.wikipedia.org/wiki/Inductive_bias))
  - A set of assumptions the model uses to make predictions of unseen inputs (think: inter- and extra-polation)
- Also see [Occam's razor](https://en.wikipedia.org/wiki/Occam's_razor): "The simplest (consistent) explanation is usually the best one."

## Miscellaneous

- [Confidence estimation](./2023-05.md#confidence-estimation)
- Data and Concept drift
  - Data drift: Input data seen in production has shifted from data used in training
  - Concept drift: Mapping from input to expected output has changed (compared to training)
    - Will need relabeling of original training data or discarding them and collect new data
- [Feature engineering](./2024-07.md#feature-engineering)
- [Feature selection](./2023-05.md#feature-selection)
- [Feature extraction](./2023-05.md#feature-extraction)
- [Data Visualization](./2023-05.md#data-visualization)
- Ethics and Bias: awareness of ethical considerations, such as privacy, fairness, and transparency in model development and deployment. Bias in data or algorithms can lead to unfair or discriminatory outcomes.
