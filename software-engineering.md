## Software Engineering

### Software Development Lifecycle

1. Requirements analysis phase:
   - Understand high-level goals
   - Functional requirements
     - Scope: use-cases and non-goals
     - Feature specifications to meet the use-cases
   - Non-functional requirements
     - Scalability and performance goals (# of users, latency, etc.),
     - Security and privacy standards
   - Set milestones for each phase
1. Exploration phase:
   - Brainstorm ideas, data exploration, quick prototyping etc.
   - Identify risks and understand feasibility
1. Design and implementation phase:
   - Document the process properly using:
     - Use-case diagrams, API design, API sequence diagrams, class diagrams, database design etc.
   - Follow test-driven development (or [another philosophy](https://en.wikipedia.org/wiki/List_of_software_development_philosophies))
1. Quality check phase: writing extensive integration tests, verification
1. Deployment and maintenance phase: ensure proper monitoring, updateability, backups, revertibility etc.

Different project management aproaches:

- **Waterfall model**: go through each phase, one at a time, in-detail. Slow deliveries, and may not keep up with changing requirements.
- **Agile model**: very short design phase; prototyping and implementation may happen simultaneously; short quality check phase. Fast deliveries, but possibly more maintenance cost due to higher chances of bugs and inflexible design decisions
- **Iterative model**: divide the project into several small deliverable milestones. Faster deliveries and user feedback opportunities. May need clever simplifications; may not always be possible to design a small deliverable for each step.
- **Spiral model**: similar to iterative model?

### Machine Learning Project Lifecycle

Source: [Intro to ML in Production](https://www.coursera.org/learn/introduction-to-machine-learning-in-production)

1. Scoping: define the project and constraints
   - Constraints: realtime or batched, cloud or edge/browser, compute resources, latency, privacy
1. Data: define, explore, collect
   - Define inputs and targets; establish rules to minimize inconsistencies
   - Explore usability of publicly available datasets
   - Collect, label and organize
1. Baseline: establish a goal
   - Define various useful metrics for evaluation (e.g.: F-score)
   - Establish baseline performance
     - Human Level Performance (HLP) for unstructured data (image, audio, natural language)
     - Performance of a quick prototype (using a small model, or a public model), or older model
1. Modeling: select, train, evaluate
   - [Model selection](https://github.com/johncf/learn-log/blob/master/ml-concepts.md#model-selection)
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

A good set of [MLOps tools](https://github.com/johncf/learn-log/blob/master/2023-05.md#mlops-tools) should make these steps as effortless as possible.
