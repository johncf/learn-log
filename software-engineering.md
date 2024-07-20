# Software Engineering

## Software Development Lifecycle

1. Objective definition phase:
   - Understand high-level goals
1. Requirements analysis phase:
   - Functional requirements
     - Scope: use-cases and non-goals
     - Feature specifications to meet the use-cases
   - Non-functional requirements
     - Scalability and performance goals (# of users, latency, etc.),
     - Security and privacy standards
   - Set milestones for each phase
1. Design and exploration phase:
   - Brainstorm ideas, data exploration, quick prototyping etc.
   - Identify risks and understand feasibility
   - Document the process properly, and plan ahead using:
     - Use-case diagrams
     - Architecture diagrams
     - API design and sequence diagrams
     - Optionally also class diagrams, database design etc.
1. Implementation phase:
   - Define deliverables and acceptance criteria
   - Project breakdown: into smaller tasks and milestones
   - Roles and responsibilities: who is responsible for what
   - Project scheduling: estimate timeline for each milestone (and task)
   - Risk assessment and contingency measures: what might go wrong, possible alternate plans
   - Resource allocation and assign (soft) deadlines
   - Follow [a development philosophy][sw-dev-phils]
1. Quality check phase: writing extensive integration tests, verification
1. Maintenance phase: ensure proper monitoring, updateability, revertibility (backups) etc.

[sw-dev-phils]: https://en.wikipedia.org/wiki/List_of_software_development_philosophies

## Machine Learning Project Lifecycle

Source: [Intro to ML in Production](https://www.coursera.org/learn/introduction-to-machine-learning-in-production)

1. Scoping: define the project and constraints
   - Constraints: realtime or batched, cloud or edge/browser, compute resources, latency, privacy
1. Baseline: establish a goal
   - Define various useful metrics for evaluation (e.g.: F-score)
   - Collect and label a small test dataset for which the model must do well on
   - Establish baseline performance
     - Human Level Performance (HLP) for unstructured data (image, audio, natural language)
     - Performance of a quick prototype (using a small model, or a public model), or older model
1. Data: define, explore, collect
   - Define inputs and targets; establish rules to minimize inconsistencies
   - Explore usability of publicly available datasets
   - Collect, label and organize
1. Modeling: select, train, evaluate
   - [Model selection](./ml-concepts.md#model-selection)
   - Error analysis
     - Try to give meaningful context "tags" for the mistakes
     - Compare with baseline performance for each tag
     - Estimate model uncertainty (confidence); how to calibrate confidence?
   - Iterate with changes to models, hyperparameters, dataset, data augmentation, feature-set, etc.
     - Have good experiment tracking system with:
       - Replicability/reproducibility (hyperparameters, dataset metadata, code/library versions etc.)
       - Results, error analysis, and summary metrics
       - Resource monitoring
     - Keeping history of failed experiments is as important as that of successful experiments
1. Deployment: deploy, then monitor & maintain
   - Shadow-mode (parallel) deployment, Canary (gradual ramp-up) deployment
1. Monitoring: to detect data drift and concept drift
   - software metrics (memory, compute, latency etc.)
   - input metrics (input length, fraction of missing values, image brightness)
   - output metrics (fraction of missing values, is null/empty/error)
   - user behavior (rerunning, switching to manual mode etc.)
   - set thresholds for notifications/alarms (for detecting drifts etc.)

A good set of [MLOps tools](./2023-05.md#mlops-tools) should make these steps as effortless as possible.
